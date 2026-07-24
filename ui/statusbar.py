"""
=========================================================
Cashier Shield AI
Status Bar
=========================================================
"""

import customtkinter as ctk


class StatusBar(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            height=38,
            corner_radius=0
        )

        self.pack_propagate(False)

        # ---------------- Left Status ---------------- #

        self.status_label = ctk.CTkLabel(
            self,
            text="🟢 Ready",
            font=("Segoe UI", 12)
        )

        self.status_label.pack(
            side="left",
            padx=15
        )

        # ---------------- Right Version ---------------- #

        self.version_label = ctk.CTkLabel(
            self,
            text="Cashier Shield AI v2.0",
            font=("Segoe UI", 12)
        )

        self.version_label.pack(
            side="right",
            padx=15
        )

    # ------------------------------------------------ #

    def set_ready(self):
        self.status_label.configure(
            text="🟢 Ready"
        )

    def set_running(self, task="Processing"):
        self.status_label.configure(
            text=f"🟡 {task}..."
        )

    def set_success(self, task="Completed"):
        self.status_label.configure(
            text=f"✅ {task}"
        )

    def set_error(self, message="Error"):
        self.status_label.configure(
            text=f"🔴 {message}"
        )

    def set_message(self, message):
        self.status_label.configure(
            text=message
        )