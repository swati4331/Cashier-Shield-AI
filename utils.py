"""
utils.py

Shared utility functions for Cashier Shield AI

Author : Shubhashree Bhat
Project : Cashier Shield AI
"""

from pathlib import Path
from datetime import datetime
import platform
import subprocess
import os

# ==========================================================
# Project Directories
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent

DATASET_DIR = BASE_DIR / "datasets"
MODEL_DIR = BASE_DIR / "models"
GRAPH_DIR = BASE_DIR / "graphs"
RESULTS_DIR = BASE_DIR / "results"

# ==========================================================
# Ensure Directories Exist
# ==========================================================

for directory in (
    DATASET_DIR,
    MODEL_DIR,
    GRAPH_DIR,
    RESULTS_DIR,
):
    directory.mkdir(exist_ok=True)

# ==========================================================
# Current Timestamp
# ==========================================================

def current_timestamp():

    return datetime.now().strftime(
        "%d-%m-%Y %I:%M:%S %p"
    )

# ==========================================================
# Alert Sound
# ==========================================================

def alert():

    """
    Cross-platform notification sound.
    """

    system = platform.system()

    try:

        if system == "Windows":

            import winsound

            winsound.Beep(1000, 500)

        elif system == "Darwin":

            os.system("afplay /System/Library/Sounds/Ping.aiff")

        else:

            print("\a")

    except Exception:

        print("\a")

# ==========================================================
# Open File
# ==========================================================

def open_file(file_path):

    file_path = Path(file_path)

    if not file_path.exists():

        return False

    system = platform.system()

    try:

        if system == "Windows":

            os.startfile(file_path)

        elif system == "Darwin":

            subprocess.call(["open", file_path])

        else:

            subprocess.call(["xdg-open", file_path])

        return True

    except Exception:

        return False

    # ==========================================================
# Divider
# ==========================================================

def divider(length=60, character="-"):

    return character * length


# ==========================================================
# Format Currency
# ==========================================================

def format_currency(amount):

    try:

        return f"₹ {float(amount):,.2f}"

    except (TypeError, ValueError):

        return str(amount)


# ==========================================================
# Format Transaction Details
# ==========================================================

def format_transaction(details):

    """
    Converts a transaction_details() dictionary
    into a readable multi-line string.
    """

    if not details.get("found", False):

        return details.get("message", "Transaction not found.")

    lines = [
        divider(),
        "TRANSACTION DETAILS",
        divider(),
        f"Transaction ID        : {details.get('transaction_id', '-')}",
        f"Amount                : {format_currency(details.get('amount', 0))}",
        f"Items                 : {details.get('items', '-')}",
        f"Manual Adjustments    : {details.get('manual_adjustments', '-')}",
        f"Refund                : {details.get('refund', '-')}",
        f"Transaction Time      : {details.get('transaction_time', '-')}",
        f"Discounts Applied     : {details.get('discounts', '-')}",
        f"Peak Hours            : {details.get('peak_hours', '-')}",
    ]

    # These keys differ between the two ML modules
    if "cashier_id" in details:
        lines.append(
            f"Cashier ID            : {details.get('cashier_id')}"
        )

    if "cashier_experience" in details:
        lines.append(
            f"Cashier Experience    : {details.get('cashier_experience')}"
        )

    if "customer_experience" in details:
        lines.append(
            f"Customer Experience   : {details.get('customer_experience')}"
        )

    lines.extend([
        f"Fraud Detected Daily  : {details.get('fraud_detected_daily', '-')}",
        f"Shift Duration        : {details.get('shift_duration', '-')}",
        f"Average Spend         : {format_currency(details.get('average_customer_spend', 0))}",
        divider(),
        f"Status                : {details.get('status', '-')}",
        divider()
    ])

    return "\n".join(lines)


# ==========================================================
# Project Information
# ==========================================================

PROJECT_INFO = {
    "name": "Cashier Shield AI",
    "version": "1.0.0",
    "developer": "Shubhashree Bhat",
    "description": (
        "AI-powered fraud detection system using "
        "Isolation Forest and Random Forest."
    )
}


# ==========================================================
# About Text
# ==========================================================

def about_text():

    return (
        f"{PROJECT_INFO['name']}\n\n"
        f"Version : {PROJECT_INFO['version']}\n\n"
        f"Developer : {PROJECT_INFO['developer']}\n\n"
        f"{PROJECT_INFO['description']}"
    )


# ==========================================================
# Public API
# ==========================================================

__all__ = [
    "BASE_DIR",
    "DATASET_DIR",
    "MODEL_DIR",
    "GRAPH_DIR",
    "RESULTS_DIR",
    "current_timestamp",
    "alert",
    "open_file",
    "divider",
    "format_currency",
    "format_transaction",
    "PROJECT_INFO",
    "about_text",
]
