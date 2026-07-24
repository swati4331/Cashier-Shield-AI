"""
=========================================================
Cashier Shield AI
Detection Controller
=========================================================

Acts as the bridge between the UI and the ML modules.
"""

from cashier_model import (
    initialize as cashier_initialize,
    model_information as cashier_info,
    total_summary as cashier_summary,
    generate_summary_graph as cashier_graph
)

from online_model import (
    initialize as online_initialize,
    model_information as online_info,
    total_summary as online_summary,
    generate_summary_graph as online_graph
)


class DetectionController:

    # =====================================================
    # Cashier Fraud Detection
    # =====================================================

    @staticmethod
    def run_cashier():

        cashier_initialize()

        return {
            "info": cashier_info(),
            "summary": cashier_summary(),
            "graph": cashier_graph()
        }

    # =====================================================
    # Online Fraud Detection
    # =====================================================

    @staticmethod
    def run_online():

        online_initialize()

        return {
            "info": online_info(),
            "summary": online_summary(),
            "graph": online_graph()
        }