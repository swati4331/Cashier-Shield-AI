"""
=========================================================
Cashier Shield AI
Sidebar
=========================================================
"""

from pathlib import Path

import customtkinter as ctk
from PIL import Image

from .theme import *


BASE_DIR = Path(__file__).resolve().parent.parent
LOGO_PATH = BASE_DIR / "assets" / "logo.png"


class Sidebar(ctk.CTkFrame):

    def __init__(self, parent, app):

        super().__init__(
            parent,
            width=SIDEBAR_WIDTH,
            corner_radius=0
        )

        self.app = app

        self.grid(row=0, column=0, sticky="ns")

        self.build_sidebar()

    # -----------------------------------------------------

    def build_sidebar(self):

        # ---------------- Logo ---------------- #

        if LOGO_PATH.exists():

            image = Image.open(LOGO_PATH)

            logo = ctk.CTkImage(
                light_image=image,
                dark_image=image,
                size=(110, 110)
            )

            logo_label = ctk.CTkLabel(
                self,
                image=logo,
                text=""
            )

            logo_label.pack(pady=(25, 10))

        # ---------------- Title ---------------- #

        ctk.CTkLabel(
            self,
            text="Cashier Shield AI",
            font=TITLE_FONT
        ).pack()

        ctk.CTkLabel(
            self,
            text="AI-Powered Retail Fraud Detection",
            font=SMALL_FONT
        ).pack(pady=(0, 25))

        # ---------------- Buttons ---------------- #

        self.create_button("🏠 Dashboard", self.app.show_dashboard)
        self.create_button("💰 Cashier Fraud", self.app.cashier_detection)
        self.create_button("🌐 Online Fraud", self.app.online_detection)
        self.create_button("📊 Reports", self.app.view_reports)
        self.create_button("🔍 Search", self.app.search_transaction)
        self.create_button("📈 Graphs", self.app.view_graph)
        self.create_button("ℹ About", self.app.show_about)

        ctk.CTkButton(
            self,
            text="Exit",
            height=BUTTON_HEIGHT,
            fg_color=DANGER,
            hover_color="#991B1B",
            command=self.app.destroy
        ).pack(
            side="bottom",
            padx=18,
            pady=25,
            fill="x"
        )

    # -----------------------------------------------------

    def create_button(self, text, command):

        ctk.CTkButton(
            self,
            text=text,
            height=BUTTON_HEIGHT,
            command=command
        ).pack(
            padx=18,
            pady=7,
            fill="x"
        )
    