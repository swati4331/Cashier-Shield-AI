"""
cashier_model.py

Cashier Fraud Detection Module
------------------------------
This module contains the complete Machine Learning logic for detecting
fraudulent cashier transactions using Isolation Forest.

Responsibilities:
- Load dataset
- Preprocess data
- Train/Load Isolation Forest model
- Predict anomalies
- Save model
- Save prediction results
- Generate summaries
- Generate graphs

Author: Shubhashree Bhat
Project: Cashier Shield AI
"""

from pathlib import Path
import pickle
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest

# ==========================================================
# Project Paths
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent

DATASET_DIR = BASE_DIR / "datasets"
MODEL_DIR = BASE_DIR / "models"
GRAPH_DIR = BASE_DIR / "graphs"
RESULTS_DIR = BASE_DIR / "results"

MODEL_DIR.mkdir(exist_ok=True)
GRAPH_DIR.mkdir(exist_ok=True)
RESULTS_DIR.mkdir(exist_ok=True)

DATASET_FILE = DATASET_DIR / "cashier_dataset.csv"

MODEL_FILE = MODEL_DIR / "cashier_isolation_model.pkl"

RESULT_FILE = RESULTS_DIR / "cashier_results.csv"

GRAPH_FILE = GRAPH_DIR / "cashier_summary_graph.png"

# ==========================================================
# Numeric Features
# ==========================================================

NUMERIC_FEATURES = [
    "Transaction_Amount",
    "Number_of_Items",
    "Manual_Adjustments",
    "Refund",
    "Transaction_Time",
    "Discounts_Applied",
    "Peak_Hours",
    "Cashier_Experience",
    "Fraud_Detected_Daily",
    "Shift_Duration",
    "Avg_Customer_Spend"
]

# ==========================================================
# Load Dataset
# ==========================================================

def load_dataset():

    if not DATASET_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found:\n{DATASET_FILE}"
        )

    data = pd.read_csv(DATASET_FILE)

    data = data.dropna()

    return data


# ==========================================================
# Preprocess Dataset
# ==========================================================

def preprocess_data(data):

    X = data[NUMERIC_FEATURES]

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    return X_scaled, scaler


# ==========================================================
# Train Isolation Forest
# ==========================================================

def train_model(X_scaled):

    model = IsolationForest(
        n_estimators=100,
        contamination=0.05,
        random_state=42
    )

    model.fit(X_scaled)

    with open(MODEL_FILE, "wb") as file:
        pickle.dump(model, file)

    return model


# ==========================================================
# Load Existing Model
# ==========================================================

def load_model():

    if MODEL_FILE.exists():

        with open(MODEL_FILE, "rb") as file:
            return pickle.load(file)

    return None


# ==========================================================
# Get Trained Model
# ==========================================================

def get_model(X_scaled):

    model = load_model()

    if model is None:

        model = train_model(X_scaled)

    return model


# ==========================================================
# Predict Anomalies
# ==========================================================

def predict_transactions():

    data = load_dataset()

    X_scaled, scaler = preprocess_data(data)

    model = get_model(X_scaled)

    predictions = model.predict(X_scaled)

    data["Anomaly"] = predictions

    data.to_csv(RESULT_FILE, index=False)

    return data

# ==========================================================
# Total Summary
# ==========================================================

def total_summary():

    data = predict_transactions()

    total_transactions = len(data)

    normal_transactions = len(
        data[data["Anomaly"] == 1]
    )

    fraud_transactions = len(
        data[data["Anomaly"] == -1]
    )

    fraud_percentage = (
        fraud_transactions / total_transactions
    ) * 100

    summary = (
        "Isolation Forest Summary\n"
        "=========================\n\n"
        f"Total Transactions : {total_transactions}\n"
        f"Normal Transactions : {normal_transactions}\n"
        f"Fraud Transactions : {fraud_transactions}\n"
        f"Fraud Percentage : {fraud_percentage:.2f}%\n"
    )

    return summary


# ==========================================================
# Generate Graph
# ==========================================================

def generate_summary_graph():

    data = predict_transactions()

    normal_transactions = len(
        data[data["Anomaly"] == 1]
    )

    fraud_transactions = len(
        data[data["Anomaly"] == -1]
    )

    plt.figure(figsize=(8,5))

    plt.bar(
        ["Normal","Fraud"],
        [normal_transactions,fraud_transactions]
    )

    plt.title("Cashier Fraud Detection Summary")

    plt.xlabel("Transaction Type")

    plt.ylabel("Count")

    plt.tight_layout()

    plt.savefig(GRAPH_FILE)

    plt.close()

    return GRAPH_FILE


# ==========================================================
# Genuine Transactions
# ==========================================================

def genuine_transactions(limit=10):

    data = predict_transactions()

    genuine = data[
        data["Anomaly"] == 1
    ].head(limit)

    return genuine


# ==========================================================
# Fraud Transactions
# ==========================================================

def fraud_transactions(limit=10):

    data = predict_transactions()

    fraud = data[
        data["Anomaly"] == -1
    ].head(limit)

    return fraud


# ==========================================================
# Transaction Summary
# ==========================================================

def transaction_summary(limit=10):

    genuine = genuine_transactions(limit)

    fraud = fraud_transactions(limit)

    genuine_text = "Genuine Transactions\n\n"

    for _, row in genuine.iterrows():

        genuine_text += (
            f"Transaction ID : {row['Transaction_ID']}\n"
            f"Cashier ID : {row['Cashier_ID']}\n"
            f"Amount : {row['Transaction_Amount']}\n\n"
        )

    fraud_text = "Fraud Transactions\n\n"

    for _, row in fraud.iterrows():

        fraud_text += (
            f"Transaction ID : {row['Transaction_ID']}\n"
            f"Cashier ID : {row['Cashier_ID']}\n"
            f"Amount : {row['Transaction_Amount']}\n\n"
        )

    return genuine_text, fraud_text

# ==========================================================
# Search Transaction By ID
# ==========================================================

def get_transaction(transaction_id):

    data = predict_transactions()

    transaction = data[
        data["Transaction_ID"].astype(str)
        == str(transaction_id)
    ]

    if transaction.empty:
        return None

    return transaction.iloc[0]


# ==========================================================
# Transaction Details
# ==========================================================

def transaction_details(transaction_id):

    transaction = get_transaction(transaction_id)

    if transaction is None:

        return {
            "found": False,
            "message": f"Transaction ID {transaction_id} not found."
        }

    fraud = transaction["Anomaly"] == -1

    status = "Fraud Detected" if fraud else "Safe Transaction"

    return {
        "found": True,
        "transaction_id": transaction["Transaction_ID"],
        "cashier_id": transaction["Cashier_ID"],
        "amount": transaction["Transaction_Amount"],
        "items": transaction["Number_of_Items"],
        "manual_adjustments": transaction["Manual_Adjustments"],
        "refund": transaction["Refund"],
        "transaction_time": transaction["Transaction_Time"],
        "discounts": transaction["Discounts_Applied"],
        "peak_hours": transaction["Peak_Hours"],
        "cashier_experience": transaction["Cashier_Experience"],
        "fraud_detected_daily": transaction["Fraud_Detected_Daily"],
        "shift_duration": transaction["Shift_Duration"],
        "average_customer_spend": transaction["Avg_Customer_Spend"],
        "status": status,
        "fraud": fraud
    }


# ==========================================================
# Model Information
# ==========================================================

def model_information():

    data = predict_transactions()

    total = len(data)

    fraud = len(data[data["Anomaly"] == -1])

    normal = len(data[data["Anomaly"] == 1])

    percentage = (fraud / total) * 100

    return {
        "algorithm": "Isolation Forest",
        "total_transactions": total,
        "normal_transactions": normal,
        "fraud_transactions": fraud,
        "fraud_percentage": round(percentage, 2),
        "model_path": str(MODEL_FILE),
        "dataset_path": str(DATASET_FILE),
        "graph_path": str(GRAPH_FILE),
        "results_path": str(RESULT_FILE)
    }


# ==========================================================
# Initialize Module
# ==========================================================

def initialize():

    """
    Train or load the model and generate
    prediction results if they do not exist.
    """

    data = predict_transactions()

    generate_summary_graph()

    return data


# ==========================================================
# Public API
# ==========================================================

__all__ = [
    "initialize",
    "predict_transactions",
    "transaction_details",
    "transaction_summary",
    "total_summary",
    "generate_summary_graph",
    "model_information",
    "genuine_transactions",
    "fraud_transactions"
]