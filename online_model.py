"""
online_model.py

Online Fraud Detection Module
-----------------------------

Uses Random Forest to detect fraudulent online transactions.

Responsibilities
----------------
- Load dataset
- Preprocess data
- Train Random Forest
- Save/Load model
- Predict fraud
- Save prediction results

Author : Shubhashree Bhat
Project : Cashier Shield AI
"""

from pathlib import Path
import pickle

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    classification_report,
    confusion_matrix
)

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

DATASET_FILE = DATASET_DIR / "online_dataset.csv"

MODEL_FILE = MODEL_DIR / "online_random_forest.pkl"

RESULT_FILE = RESULTS_DIR / "online_results.csv"

GRAPH_FILE = GRAPH_DIR / "online_summary_graph.png"

# ==========================================================
# Feature Columns
# ==========================================================

FEATURE_COLUMNS = [
    "Transaction_Amount",
    "Number_of_Items",
    "Manual_Adjustments",
    "Refund",
    "Discounts_Applied",
    "Peak_Hours",
    "Cashier_Experience",
    "Fraud_Detected_Daily",
    "Shift_Duration",
    "Avg_Customer_Spend",
    "Transaction_Time"
]

TARGET_COLUMN = "Fraud"

# ==========================================================
# Load Dataset
# ==========================================================

def load_dataset():

    if not DATASET_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found:\n{DATASET_FILE}"
        )

    data = pd.read_csv(DATASET_FILE)

    data["Transaction_Time"] = pd.to_datetime(
        data["Transaction_Time"]
    )

    data["Transaction_Time"] = (
        data["Transaction_Time"].astype(np.int64)
        // 10**9
    )

    data = data.dropna()

    return data

# ==========================================================
# Prepare Data
# ==========================================================

def prepare_data(data):

    X = data[FEATURE_COLUMNS]

    y = data[TARGET_COLUMN]

    return train_test_split(
        X,
        y,
        test_size=0.30,
        random_state=42
    )

# ==========================================================
# Train Model
# ==========================================================

def train_model():

    data = load_dataset()

    X_train, X_test, y_train, y_test = prepare_data(data)

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

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

    return train_model()

# ==========================================================
# Prediction
# ==========================================================

def predict_transactions():

    data = load_dataset()

    model = load_model()

    X = data[FEATURE_COLUMNS]

    data["Fraud_Prediction"] = model.predict(X)

    data.to_csv(RESULT_FILE, index=False)

    return data

# ==========================================================
# Classification Report
# ==========================================================

def evaluation_report():

    data = load_dataset()

    X_train, X_test, y_train, y_test = prepare_data(data)

    model = load_model()

    predictions = model.predict(X_test)

    report = classification_report(
        y_test,
        predictions
    )

    matrix = confusion_matrix(
        y_test,
        predictions
    )

    return report, matrix


# ==========================================================
# Total Summary
# ==========================================================

def total_summary():

    data = predict_transactions()

    total_transactions = len(data)

    normal_transactions = len(
        data[data["Fraud_Prediction"] == 0]
    )

    fraud_transactions = len(
        data[data["Fraud_Prediction"] == 1]
    )

    fraud_percentage = (
        fraud_transactions / total_transactions
    ) * 100

    summary = (
        "Random Forest Summary\n"
        "=========================\n\n"
        f"Total Transactions : {total_transactions}\n"
        f"Normal Transactions : {normal_transactions}\n"
        f"Fraud Transactions : {fraud_transactions}\n"
        f"Fraud Percentage : {fraud_percentage:.2f}%\n"
    )

    return summary


# ==========================================================
# Generate Summary Graph
# ==========================================================

def generate_summary_graph():

    data = predict_transactions()

    normal_transactions = len(
        data[data["Fraud_Prediction"] == 0]
    )

    fraud_transactions = len(
        data[data["Fraud_Prediction"] == 1]
    )

    plt.figure(figsize=(8, 5))

    plt.bar(
        ["Normal", "Fraud"],
        [normal_transactions, fraud_transactions]
    )

    plt.title("Online Fraud Detection Summary")

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

    return data[
        data["Fraud_Prediction"] == 0
    ].head(limit)


# ==========================================================
# Fraud Transactions
# ==========================================================

def fraud_transactions(limit=10):

    data = predict_transactions()

    return data[
        data["Fraud_Prediction"] == 1
    ].head(limit)


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
            f"Amount : {row['Transaction_Amount']}\n\n"
        )

    fraud_text = "Fraud Transactions\n\n"

    for _, row in fraud.iterrows():

        fraud_text += (
            f"Transaction ID : {row['Transaction_ID']}\n"
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

    fraud = transaction["Fraud_Prediction"] == 1

    status = "Fraud Detected" if fraud else "Safe Transaction"

    return {
        "found": True,
        "transaction_id": transaction["Transaction_ID"],
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

    fraud = len(
        data[data["Fraud_Prediction"] == 1]
    )

    normal = len(
        data[data["Fraud_Prediction"] == 0]
    )

    percentage = (fraud / total) * 100

    return {
        "algorithm": "Random Forest",
        "total_transactions": total,
        "normal_transactions": normal,
        "fraud_transactions": fraud,
        "fraud_percentage": round(percentage, 2),
        "model_path": str(MODEL_FILE),
        "dataset_path": str(DATASET_FILE),
        "results_path": str(RESULT_FILE),
        "graph_path": str(GRAPH_FILE)
    }


# ==========================================================
# Initialize Module
# ==========================================================

def initialize():

    """
    Train or load the model,
    generate predictions and graph.
    """

    predict_transactions()

    generate_summary_graph()

    return True


# ==========================================================
# Public API
# ==========================================================

__all__ = [
    "initialize",
    "predict_transactions",
    "transaction_details",
    "transaction_summary",
    "evaluation_report",
    "total_summary",
    "generate_summary_graph",
    "model_information",
    "genuine_transactions",
    "fraud_transactions"
]