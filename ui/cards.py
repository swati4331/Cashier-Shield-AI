"""
=========================================================
Cashier Shield AI
Dashboard Cards
=========================================================
"""

import customtkinter as ctk
from .theme import *


class DashboardCard(ctk.CTkFrame):

    def __init__(
        self,
        parent,
        title,
        value="--",
        icon="📊"
    ):

        super().__init__(
            parent,
            corner_radius=18,
            fg_color="#2B2B2B",
            border_width=1,
            border_color="#3A3A3A"
        )

        self.title = title
        self.icon = icon

        self.grid_propagate(False)

        # ---------------- Icon ---------------- #

        self.icon_label = ctk.CTkLabel(
            self,
            text=icon,
            font=("Segoe UI Emoji", 30)
        )
        self.icon_label.pack(pady=(15, 5))

        # ---------------- Title ---------------- #

        self.title_label = ctk.CTkLabel(
            self,
            text=title,
            font=("Segoe UI", 15, "bold")
        )
        self.title_label.pack()

        # ---------------- Value ---------------- #

        self.value_label = ctk.CTkLabel(
            self,
            text=value,
            font=("Segoe UI", 30, "bold"),
            text_color="#4FC3F7"
        )
        self.value_label.pack(pady=(12, 20))

    # ---------------- Update ---------------- #

    def set_value(self, value):
        self.value_label.configure(text=str(value))

    def set_title(self, title):
        self.title_label.configure(text=title)

    def set_icon(self, icon):
        self.icon_label.configure(text=icon)