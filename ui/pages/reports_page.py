import customtkinter as ctk

from cashier_model import (
    model_information as cashier_info,
    transaction_summary as cashier_summary,
    fraud_transactions as cashier_fraud,
)

from online_model import (
    model_information as online_info,
    transaction_summary as online_summary,
    fraud_transactions as online_fraud,
)


class ReportsPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.pack_propagate(False)

        # ==========================
        # Title
        # ==========================

        title = ctk.CTkLabel(
            self,
            text="📊 Reports Dashboard",
            font=("Segoe UI", 30, "bold")
        )
        title.pack(pady=(20, 10))

        subtitle = ctk.CTkLabel(
            self,
            text="Machine Learning Fraud Detection Summary",
            font=("Segoe UI", 14)
        )
        subtitle.pack(pady=(0, 20))

        # ==========================
        # Cashier Report
        # ==========================

        cashier_title = ctk.CTkLabel(
            self,
            text="💰 Cashier Fraud Report",
            font=("Segoe UI", 18, "bold")
        )
        cashier_title.pack(anchor="w", padx=30)

        self.cashier_text = ctk.CTkTextbox(
            self,
            width=900,
            height=170,
            corner_radius=12,
            border_width=1
        )
        self.cashier_text.pack(padx=30, pady=(5, 15))

        # ==========================
        # Online Report
        # ==========================

        online_title = ctk.CTkLabel(
            self,
            text="🌐 Online Fraud Report",
            font=("Segoe UI", 18, "bold")
        )
        online_title.pack(anchor="w", padx=30)

        self.online_text = ctk.CTkTextbox(
            self,
            width=900,
            height=170,
            corner_radius=12,
            border_width=1
        )
        self.online_text.pack(padx=30, pady=(5, 15))

        # ==========================
        # Fraud Activity
        # ==========================

        fraud_title = ctk.CTkLabel(
            self,
            text="⚠ Recent Fraud Transactions",
            font=("Segoe UI", 18, "bold")
        )
        fraud_title.pack(anchor="w", padx=30)

        self.activity = ctk.CTkTextbox(
            self,
            width=900,
            height=170,
            corner_radius=12,
            border_width=1
        )
        self.activity.pack(padx=30, pady=(5, 20))

        # ==========================
        # Refresh Button
        # ==========================

        refresh = ctk.CTkButton(
            self,
            text="🔄 Refresh Reports",
            width=220,
            height=42,
            corner_radius=12,
            font=("Segoe UI", 14, "bold"),
            command=self.load_reports
        )

        refresh.pack(pady=(0, 20))

        self.load_reports()

    def load_reports(self):

        self.cashier_text.configure(state="normal")
        self.online_text.configure(state="normal")
        self.activity.configure(state="normal")

        self.cashier_text.delete("1.0", "end")
        self.online_text.delete("1.0", "end")
        self.activity.delete("1.0", "end")

        # ==========================
        # Cashier Report
        # ==========================

        info = cashier_info()

        self.cashier_text.insert(
            "end",
            f"Algorithm : {info['algorithm']}\n\n"
        )

        self.cashier_text.insert(
            "end",
            cashier_summary()
        )

        # ==========================
        # Online Report
        # ==========================

        info = online_info()

        self.online_text.insert(
            "end",
            f"Algorithm : {info['algorithm']}\n\n"
        )

        self.online_text.insert(
            "end",
            online_summary()
        )

        # ==========================
        # Fraud Activity
        # ==========================

        self.activity.insert(
            "end",
            "========== Cashier Fraud Transactions ==========\n\n"
        )

        self.activity.insert(
            "end",
            cashier_fraud()
        )

        self.activity.insert(
            "end",
            "\n\n========== Online Fraud Transactions ==========\n\n"
        )

        self.activity.insert(
            "end",
            online_fraud()
        )

        self.cashier_text.configure(state="disabled")
        self.online_text.configure(state="disabled")
        self.activity.configure(state="disabled")