import customtkinter as ctk
from PIL import Image

from cashier_model import generate_summary_graph as cashier_graph
from online_model import generate_summary_graph as online_graph


class GraphsPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        title = ctk.CTkLabel(
            self,
            text="Fraud Analysis Graphs",
            font=("Arial",24,"bold")
        )
        title.pack(pady=20)

        self.cashier_label = ctk.CTkLabel(self, text="")
        self.cashier_label.pack(pady=15)

        self.online_label = ctk.CTkLabel(self, text="")
        self.online_label.pack(pady=15)

        refresh = ctk.CTkButton(
            self,
            text="Refresh Graphs",
            command=self.load_graphs
        )

        refresh.pack(pady=20)

        self.load_graphs()

    def load_graphs(self):

        cashier_path = cashier_graph()
        online_path = online_graph()

        cashier_image = ctk.CTkImage(
            Image.open(cashier_path),
            size=(600,300)
        )

        online_image = ctk.CTkImage(
            Image.open(online_path),
            size=(600,300)
        )

        self.cashier_label.configure(image=cashier_image)
        self.cashier_label.image = cashier_image

        self.online_label.configure(image=online_image)
        self.online_label.image = online_image