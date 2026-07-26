import customtkinter as ctk

from cashier_model import transaction_details as cashier_transaction
from online_model import transaction_details as online_transaction


class SearchPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.pack_propagate(False)

        # =====================================================
        # TITLE
        # =====================================================

        title = ctk.CTkLabel(
            self,
            text="🔍 Transaction Search",
            font=("Segoe UI", 30, "bold")
        )
        title.pack(pady=(20, 5))

        subtitle = ctk.CTkLabel(
            self,
            text="Search Cashier or Online Transactions",
            font=("Segoe UI", 14)
        )
        subtitle.pack(pady=(0, 20))

        # =====================================================
        # SEARCH CARD
        # =====================================================

        search_frame = ctk.CTkFrame(
            self,
            corner_radius=15
        )
        search_frame.pack(padx=30, pady=10, fill="x")

        label = ctk.CTkLabel(
            search_frame,
            text="Transaction ID",
            font=("Segoe UI", 16, "bold")
        )
        label.pack(anchor="w", padx=20, pady=(20, 8))

        self.entry = ctk.CTkEntry(
            search_frame,
            width=450,
            height=40,
            corner_radius=10,
            placeholder_text="Enter Transaction ID (Example : TXN001)"
        )
        self.entry.pack(padx=20, pady=(0, 20))

        # =====================================================
        # BUTTONS
        # =====================================================

        button_frame = ctk.CTkFrame(
            search_frame,
            fg_color="transparent"
        )
        button_frame.pack(pady=(0, 20))

        cashier_btn = ctk.CTkButton(
            button_frame,
            text="💰 Search Cashier",
            width=180,
            height=40,
            corner_radius=10,
            font=("Segoe UI", 14, "bold"),
            command=self.search_cashier
        )

        cashier_btn.pack(side="left", padx=15)

        online_btn = ctk.CTkButton(
            button_frame,
            text="🌐 Search Online",
            width=180,
            height=40,
            corner_radius=10,
            font=("Segoe UI", 14, "bold"),
            command=self.search_online
        )

        online_btn.pack(side="left", padx=15)

        # =====================================================
        # RESULT TITLE
        # =====================================================

        result_title = ctk.CTkLabel(
            self,
            text="📄 Transaction Details",
            font=("Segoe UI", 22, "bold")
        )
        result_title.pack(pady=(15, 10))

        # =====================================================
        # RESULT BOX
        # =====================================================

        self.result = ctk.CTkTextbox(
            self,
            width=920,
            height=380,
            corner_radius=12,
            border_width=1,
            font=("Consolas", 14)
        )

        self.result.pack(padx=30, pady=(0, 20))

        self.result.configure(state="disabled")

    # =====================================================

    def search_cashier(self):

        transaction_id = self.entry.get().strip()

        if transaction_id == "":
            return

        details = cashier_transaction(transaction_id)

        self.display(details)

    # =====================================================

    def search_online(self):

        transaction_id = self.entry.get().strip()

        if transaction_id == "":
            return

        details = online_transaction(transaction_id)

        self.display(details)

    # =====================================================

    def display(self, details):

        self.result.configure(state="normal")

        self.result.delete("1.0", "end")

        if not details["found"]:

            self.result.insert(
                    "end",
                    "\n\n"
                    "            ❌ TRANSACTION NOT FOUND\n\n"
                    "------------------------------------------------------------\n\n"
                    f"{details['message']}\n"
                )

            self.result.configure(state="disabled")
            return

        status = details["status"]

        risk = "🔴 HIGH" if details["fraud"] else "🟢 LOW"

        divider = "=" * 65

        self.result.insert(
                "end",
                f"{divider}\n"
                "                 TRANSACTION DETAILS\n"
                f"{divider}\n\n"
            )

        text = ""

        text += f"{'Transaction ID':28}: {details['transaction_id']}\n"

        if "cashier_id" in details:
            text += f"{'Cashier ID':28}: {details['cashier_id']}\n"

        text += (
            f"{'Transaction Amount':28}: ₹{details['amount']}\n"
            f"{'Number of Items':28}: {details['items']}\n"
            f"{'Manual Adjustments':28}: {details['manual_adjustments']}\n"
            f"{'Refund':28}: {details['refund']}\n"
            f"{'Transaction Time':28}: {details['transaction_time']}\n"
            f"{'Discount Applied':28}: {details['discounts']}\n"
            f"{'Peak Hours':28}: {details['peak_hours']}\n"
            f"{'Cashier Experience':28}: {details['cashier_experience']}\n"
            f"{'Fraud Detected Daily':28}: {details['fraud_detected_daily']}\n"
            f"{'Shift Duration':28}: {details['shift_duration']}\n"
            f"{'Average Customer Spend':28}: ₹{details['average_customer_spend']}\n"
        )

        self.result.insert("end", text)

        self.result.insert(
                "end",
                "\n"
                + "-" * 65 +
                "\n\n"
            )

        self.result.insert(
                "end",
                f"{'Transaction Status':28}: {status}\n"
                f"{'Risk Level':28}: {risk}\n"
            )

        self.result.insert(
                "end",
                "\n"
                + divider +
                "\n"
            )

        self.result.configure(state="disabled")
