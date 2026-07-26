"""
=========================================================
Cashier Shield AI
Professional Dashboard
=========================================================
"""

import customtkinter as ctk

from .theme import *
from .sidebar import Sidebar
from .cards import DashboardCard
from .console import ActivityConsole
from .statusbar import StatusBar
from .graph_frame import GraphFrame
from .pages.reports_page import ReportsPage
from .pages.search_page import SearchPage
from .pages.graphs_page import GraphsPage
from .pages.about_page import AboutPage
from controllers.detection_controller import DetectionController

from cashier_model import (
    model_information as cashier_info,
    transaction_summary as cashier_summary
)

from online_model import (
    model_information as online_info,
    transaction_summary as online_summary
)


class DashboardApp(ctk.CTk):

    def __init__(self):

        super().__init__()

        # ---------------- Window ---------------- #

        self.title(APP_TITLE)

        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        self.minsize(MIN_WIDTH, MIN_HEIGHT)

        self.configure(fg_color=BACKGROUND)

        # ---------------- Grid ---------------- #

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ---------------- Sidebar ---------------- #

        self.sidebar = Sidebar(self, self)

        # ---------------- Main Area ---------------- #

        self.main = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color=BACKGROUND
        )

        self.main.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        self.main.grid_columnconfigure(0, weight=1)
        self.main.grid_rowconfigure(3, weight=1)

        # ---------------- Build UI ---------------- #

        self.build_topbar()

        self.build_cards()

        self.build_graph()

        self.build_console()

        self.build_statusbar()

    # =====================================================
    # TOP BAR
    # =====================================================

    def build_topbar(self):

        self.topbar = ctk.CTkFrame(
            self.main,
            height=90,
            corner_radius=15
        )

        self.topbar.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=20,
            pady=(20,10)
        )

        self.topbar.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(
            self.topbar,
            text="🛡 Cashier Shield AI",
            font=("Segoe UI",28,"bold")
        )

        title.grid(
            row=0,
            column=0,
            sticky="w",
            padx=20,
            pady=(15,0)
        )

        subtitle = ctk.CTkLabel(
            self.topbar,
            text="AI Powered Retail Fraud Detection Platform",
            font=("Segoe UI",14)
        )

        subtitle.grid(
            row=1,
            column=0,
            sticky="w",
            padx=20,
            pady=(0,15)
        )

        self.ready_label = ctk.CTkLabel(
            self.topbar,
            text="🟢 Ready",
            font=("Segoe UI",14,"bold")
        )

        self.ready_label.grid(
            row=0,
            column=1,
            rowspan=2,
            padx=20
        )

    # =====================================================
    # DASHBOARD CARDS
    # =====================================================

    def build_cards(self):

        self.card_frame = ctk.CTkFrame(
            self.main,
            fg_color="transparent"
        )

        self.card_frame.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=20,
            pady=10
        )

        for i in range(4):
            self.card_frame.grid_columnconfigure(i, weight=1)

        self.total_card = DashboardCard(
            self.card_frame,
            "Transactions",
            "--",
            "💳"
        )

        self.total_card.grid(
            row=0,
            column=0,
            padx=8,
            sticky="ew"
        )

        self.fraud_card = DashboardCard(
            self.card_frame,
            "Fraud",
            "--",
            "🚨"
        )

        self.fraud_card.grid(
            row=0,
            column=1,
            padx=8,
            sticky="ew"
        )

        self.normal_card = DashboardCard(
            self.card_frame,
            "Genuine",
            "--",
            "✅"
        )

        self.normal_card.grid(
            row=0,
            column=2,
            padx=8,
            sticky="ew"
        )

        self.model_card = DashboardCard(
            self.card_frame,
            "Model",
            "--",
            "🤖"
        )

        self.model_card.grid(
            row=0,
            column=3,
            padx=8,
            sticky="ew"
        )

    # =====================================================
    # GRAPH + CONSOLE
    # =====================================================

    def build_graph(self):

        self.graph_frame = GraphFrame(self.main)

        self.graph_frame.grid(
            row=2,
            column=0,
            sticky="nsew",
            padx=20,
            pady=(10,5)
        )

    def build_console(self):

        self.console = ActivityConsole(self.main)

        self.console.grid(
            row=3,
            column=0,
            sticky="nsew",
            padx=20,
            pady=(5,10)
        )

    # =====================================================
    # STATUS BAR
    # =====================================================

    def build_statusbar(self):

        self.status = StatusBar(self.main)

        self.status.grid(
            row=4,
            column=0,
            sticky="ew"
        )

     # =====================================================
    # CALLBACKS
    # =====================================================

    def show_dashboard(self):
        for page in [
        "report_page",
        "search_page",
        "graph_page",
        "about_page"
    ]:

            if hasattr(self, page):
                getattr(self, page).destroy()
                delattr(self, page)
        
        self.topbar.grid()
        self.card_frame.grid()
        self.graph_frame.grid()
        self.console.grid()
        self.status.grid()
        self.console.log("Dashboard opened.")
        self.status.set_ready()


    def cashier_detection(self):

        try:
            self.status.set_running()
            self.console.log("Loading Cashier Fraud Detection...")

            result = DetectionController.run_cashier()
            info = result["info"]

            # Update Cards
            self.total_card.set_value(info["total_transactions"])
            self.fraud_card.set_value(info["fraud_transactions"])
            self.normal_card.set_value(info["normal_transactions"])
            self.model_card.set_value(info["algorithm"])

            # Show Graph
            self.graph_frame.show_graph(result["graph"])

            # Console
            self.console.log("Cashier Detection Completed.")
            self.console.log(result["summary"])

            self.status.set_success()

        except Exception as e:
            self.console.log(f"ERROR: {e}")
            self.status.set_error()


    def online_detection(self):
        
        try:
            self.status.set_running()
            self.console.log("Loading Online Fraud Detection...")

            result = DetectionController.run_online()
            info = result["info"]

            # Update Cards
            self.total_card.set_value(info["total_transactions"])
            self.fraud_card.set_value(info["fraud_transactions"])
            self.normal_card.set_value(info["normal_transactions"])
            self.model_card.set_value(info["algorithm"])

            # Show Graph
            self.graph_frame.show_graph(result["graph"])

            # Console
            self.console.log("Online Detection Completed.")
            self.console.log(result["summary"])

            self.status.set_success()

        except Exception as e:
            import traceback
            traceback.print_exc()          # Prints the full error in the terminal
            print(e)
            self.console.log(f"ERROR: {e}")
            self.status.set_error()


    def view_reports(self):
        self.topbar.grid_remove()
        self.card_frame.grid_remove()
        self.graph_frame.grid_remove()
        self.console.grid_remove()
        self.status.grid_remove()
        self.report_page = ReportsPage(self.main)
        self.report_page.grid(
            row=0,
            column=0,
            rowspan=5,
            sticky="nsew",
            padx=10,
            pady=10
            )


    def search_transaction(self):

        self.topbar.grid_remove()
        self.card_frame.grid_remove()
        self.graph_frame.grid_remove()
        self.console.grid_remove()
        self.status.grid_remove()

        if hasattr(self, "report_page"):
            self.report_page.destroy()

        if hasattr(self, "graph_page"):
            self.graph_page.destroy()

        if hasattr(self, "about_page"):
            self.about_page.destroy()

        self.search_page = SearchPage(self.main)

        self.search_page.grid(
            row=0,
            column=0,
            rowspan=5,
            sticky="nsew"
        )


    def view_graph(self):
        self.topbar.grid_remove()
        self.card_frame.grid_remove()
        self.graph_frame.grid_remove()
        self.console.grid_remove()
        self.status.grid_remove()
        for page in [
            "report_page",
            "search_page",
            "about_page"
        ]:
                if hasattr(self, page):
                    getattr(self, page).destroy()

        self.graph_page = GraphsPage(self.main)
        self.graph_page.grid(
            row=0,
            column=0,
            rowspan=5,
            sticky="nsew"
        )


    def show_about(self):

        self.topbar.grid_remove()
        self.card_frame.grid_remove()
        self.graph_frame.grid_remove()
        self.console.grid_remove()
        self.status.grid_remove()

        for page in [
            "report_page",
            "search_page",
            "graph_page"
        ]:

            if hasattr(self, page):
                getattr(self, page).destroy()

        self.about_page = AboutPage(self.main)

        self.about_page.grid(
            row=0,
            column=0,
            rowspan=5,
            sticky="nsew"
        )