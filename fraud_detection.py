import streamlit as st
import pandas as pd
import joblib
import numpy as np

model = joblib.load("fraud_detection_model.joblib")

st.title("💰 Fraud Detection Prediction App")
st.markdown("Detect potentially fraudulent transactions using machine learning")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Transaction Details")
    transaction_type = st.selectbox("Transaction Type", 
                                ["PAYMENT", "TRANSFER", "CASH_OUT", "DEBIT", "CASH_IN"])
    amount = st.number_input("Amount", min_value=0.0, value=1000.0, step=100.0,
                        help="Transaction amount in currency units")

with col2:
    st.subheader("Balance Information")
    oldbalanceOrg = st.number_input("Origin Old Balance", min_value=0.0, value=10000.0, step=1000.0)
    newbalanceOrig = st.number_input("Origin New Balance", min_value=0.0, value=9000.0, step=1000.0)
    oldbalanceDest = st.number_input("Destination Old Balance", min_value=0.0, value=0.0, step=1000.0)
    newbalanceDest = st.number_input("Destination New Balance", min_value=0.0, value=0.0, step=1000.0)

st.divider()

if st.button("Predict Fraud", type="primary"):
    balanceDiffOrig = oldbalanceOrg - newbalanceOrig
    balanceDiffDest = newbalanceDest - oldbalanceDest
    
    balance_ratio_orig = (oldbalanceOrg + 1) / (newbalanceOrig + 1)
    balance_ratio_dest = (oldbalanceDest + 1) / (newbalanceDest + 1)
    amount_to_balance_orig = amount / (oldbalanceOrg + 1)
    amount_to_balance_dest = amount / (oldbalanceDest + 1)

    input_data = pd.DataFrame({
        "type": [transaction_type],
        "amount": [amount],
        "oldbalanceOrg": [oldbalanceOrg],
        "newbalanceOrig": [newbalanceOrig],
        "oldbalanceDest": [oldbalanceDest],
        "newbalanceDest": [newbalanceDest],
        "isFlaggedFraud": [0],  
        "balanceDiffOrig": [balanceDiffOrig],
        "balanceDiffDest": [balanceDiffDest],
        "balance_ratio_orig": [balance_ratio_orig],
        "balance_ratio_dest": [balance_ratio_dest],
        "amount_to_balance_orig": [amount_to_balance_orig],
        "amount_to_balance_dest": [amount_to_balance_dest]
    })
    
    try:
        prediction = model.predict(input_data)
        prediction_proba = model.predict_proba(input_data)
        
        st.subheader("Prediction Results")
        
        if prediction[0] == 1:
            st.error("🚨 This transaction is likely fraudulent!")
            st.metric("Fraud Probability", f"{prediction_proba[0][1]:.2%}")
        else:
            st.success("✅ This transaction appears legitimate")
            st.metric("Fraud Probability", f"{prediction_proba[0][1]:.2%}")
        
        st.info("💡 Tip: Transactions with unusual amounts or balance patterns are more likely to be fraudulent")
        
    except Exception as e:
        st.error(f"Error making prediction: {str(e)}")

st.divider()
st.subheader("About This App")
st.markdown("""
This fraud detection system uses a machine learning model trained on historical transaction data.
The model analyzes patterns in transaction characteristics to identify potentially fraudulent activity.

**Note:** This is a demonstration tool and should be used in conjunction with other fraud detection measures.
""")