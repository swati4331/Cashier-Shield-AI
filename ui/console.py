"""
=========================================================
Cashier Shield AI
Activity Console
=========================================================
"""

import customtkinter as ctk
from datetime import datetime


class ActivityConsole(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            corner_radius=15
        )

        # ---------------- Title ---------------- #

        title = ctk.CTkLabel(
            self,
            text="📋 Activity Console",
            font=("Segoe UI", 16, "bold")
        )

        title.pack(
            anchor="w",
            padx=15,
            pady=(12, 8)
        )

        # ---------------- Console ---------------- #

        self.console = ctk.CTkTextbox(
            self,
            font=("Consolas", 12),
            wrap="word"
        )

        self.console.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 15)
        )

        self.console.insert(
            "end",
            "Cashier Shield AI started successfully.\n"
        )

        self.console.configure(state="disabled")

    # ------------------------------------------------ #

    def log(self, message):

        timestamp = datetime.now().strftime("%H:%M:%S")

        self.console.configure(state="normal")

        self.console.insert(
            "end",
            f"[{timestamp}] {message}\n"
        )

        self.console.see("end")

        self.console.configure(state="disabled")

    # ------------------------------------------------ #

    def clear(self):

        self.console.configure(state="normal")

        self.console.delete("1.0", "end")

        self.console.configure(state="disabled")