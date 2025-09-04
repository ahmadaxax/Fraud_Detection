# Fraud Detection Analysis

## 📌 Overview

This project provides a **comprehensive analysis of financial transaction data** to detect fraudulent activities. It covers **data exploration, visualization, and a machine learning model**, deployed through a **user-friendly Streamlit application**.

---

## 🚀 Features

- **Data Analysis**: Exploratory analysis of transaction patterns and fraud indicators
- **Visualizations**: Interactive charts showing transaction distributions and fraud patterns
- **Machine Learning Model**: Fraud detection model with real-time predictions
- **Streamlit Web Application**: User-friendly interface to interact with the model

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/ahmadaxax/Fraud_Detection.git
cd fraud-detection-analysis
```

### Install required dependencies

```bash
pip install -r requirements.txt
```

### Required Packages

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- streamlit
- jupyter

---

## 📂 Usage

### Running the Analysis

Open and run the Jupyter notebook:

```bash
jupyter notebook analysis_model.ipynb
```

### Using the Streamlit App

Launch the fraud detection application:

```bash
streamlit run fraud_detection.py
```

The web interface allows you to:

- Upload transaction data
- View analysis results
- Get fraud predictions
- Explore transaction patterns

---

## 📊 Dataset

The analysis uses the **`AIML Dataset.csv`** file containing:

- Transaction details (amount, type, origin/destination accounts)
- Balance information before and after transactions
- Fraud labels (`isFraud`, `isFlaggedFraud`)

**Key Statistics:**

- Total transactions: **6,362,620**
- Fraud rate: **0.13%**
- Transaction types: `PAYMENT`, `TRANSFER`, `CASH_OUT`, etc.

You can download the dataset from Kaggle:
https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset?resource=download

---

## 🤖 Model Details

The fraud detection model is designed with the following characteristics:

- Handles **class imbalance** (fraudulent transactions are rare)
- Considers **transaction patterns and amounts**
- Provides **probability scores** for fraud likelihood

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the project
2. Create a feature branch

```bash
git checkout -b feature/AmazingFeature
```

3. Commit changes

```bash
git commit -m 'Add AmazingFeature'
```

4. Push to branch

```bash
git push origin feature/AmazingFeature
```

5. Open a Pull Request

---

## 🔧 Troubleshooting

- **Missing dependencies** → Ensure all packages in `requirements.txt` are installed
- **Data format issues** → Verify the CSV follows the expected format
- **Memory errors** → Dataset is large; ensure sufficient system resources

For additional support, please open an issue in the repository.

---

## Optional: `requirements.txt` suggestion

If you want a ready `requirements.txt` you can add the following (adjust versions if needed):

```
pandas>=1.5.0
numpy>=1.24.0
matplotlib>=3.7.0
seaborn>=0.12.0
scikit-learn>=1.2.0
streamlit>=1.25.0
jupyter>=1.0.0
```

Feel free to edit versions to match your environment.
