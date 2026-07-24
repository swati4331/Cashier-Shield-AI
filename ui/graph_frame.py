"""
=========================================================
Cashier Shield AI
Graph Frame
=========================================================
"""

import os
import customtkinter as ctk
from PIL import Image


class GraphFrame(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            corner_radius=15
        )

        # ---------------- Title ---------------- #

        title = ctk.CTkLabel(
            self,
            text="📈 Graph Preview",
            font=("Segoe UI", 16, "bold")
        )

        title.pack(
            anchor="w",
            padx=15,
            pady=(12, 8)
        )

        # ---------------- Image ---------------- #

        self.image_label = ctk.CTkLabel(
            self,
            text="No graph available",
            width=650,
            height=300
        )

        self.image_label.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 15)
        )

        self.current_image = None

    # ------------------------------------------------ #

    def show_graph(self, image_path):

        if not image_path:
            return

        if not os.path.exists(image_path):
            return

        image = Image.open(image_path)

        self.current_image = ctk.CTkImage(
            light_image=image,
            dark_image=image,
            size=(700, 350)
        )

        self.image_label.configure(
            image=self.current_image,
            text=""
        )

    # ------------------------------------------------ #

    def clear(self):

        self.image_label.configure(
            image=None,
            text="No graph available"
        )

        self.current_image = None