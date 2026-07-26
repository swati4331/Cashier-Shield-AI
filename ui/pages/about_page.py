import customtkinter as ctk


class AboutPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent, fg_color="#1B1B1B")

        self.pack(fill="both", expand=True)

        # =====================================================
        # TITLE
        # =====================================================

        title = ctk.CTkLabel(
            self,
            text="🛡️ CASHIER SHIELD AI",
            font=("Segoe UI", 30, "bold"),
            text_color="#4CC9F0"
        )
        title.pack(pady=(20, 5))

        subtitle = ctk.CTkLabel(
            self,
            text="Intelligent Fraud Detection System",
            font=("Segoe UI", 16),
            text_color="lightgray"
        )
        subtitle.pack()

        version = ctk.CTkLabel(
            self,
            text="Version 1.0",
            font=("Segoe UI", 12),
            text_color="#9CA3AF"
        )
        version.pack(pady=(0, 20))

        # =====================================================
        # MAIN CONTAINER
        # =====================================================

        body = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        body.pack(fill="both", expand=True, padx=25)

        # =====================================================
        # ROW 1
        # =====================================================

        row1 = ctk.CTkFrame(body, fg_color="transparent")
        row1.pack(fill="x", pady=10)

        developer = ctk.CTkFrame(
            row1,
            corner_radius=15,
            fg_color="#2B2B2B",
            width=320,
            height=170
        )
        developer.pack(side="left", padx=10)
        developer.pack_propagate(False)

        ctk.CTkLabel(
            developer,
            text="👩‍💻 Developer",
            font=("Segoe UI", 18, "bold"),
            text_color="#4CC9F0"
        ).pack(anchor="w", padx=20, pady=(15, 10))

        ctk.CTkLabel(
            developer,
            text="Shubhashree Bhat\n\n"
                 "Artificial Intelligence & Data Science\n\n"
                 "S.G. Balekundri Institute of Technology",
            justify="left",
            font=("Segoe UI", 13)
        ).pack(anchor="w", padx=20)

        overview = ctk.CTkFrame(
            row1,
            corner_radius=15,
            fg_color="#2B2B2B"
        )
        overview.pack(side="left", fill="both", expand=True, padx=10)

        ctk.CTkLabel(
            overview,
            text="📋 Project Overview",
            font=("Segoe UI", 18, "bold"),
            text_color="#4CC9F0"
        ).pack(anchor="w", padx=20, pady=(15, 10))

        ctk.CTkLabel(
            overview,
            text=(
                "Cashier Shield AI is a Machine Learning-based desktop "
                "application designed to detect suspicious cashier and "
                "online transactions. It provides real-time fraud "
                "analysis, transaction search, reports, and graphical "
                "visualization to assist organizations in identifying "
                "potential fraudulent activities."
            ),
            wraplength=520,
            justify="left",
            font=("Segoe UI", 13)
        ).pack(anchor="w", padx=20, pady=(0, 15))

        # =====================================================
        # ROW 2
        # =====================================================

        row2 = ctk.CTkFrame(body, fg_color="transparent")
        row2.pack(fill="x", pady=10)

        tech = ctk.CTkFrame(
            row2,
            corner_radius=15,
            fg_color="#2B2B2B",
            width=420,
            height=220
        )
        tech.pack(side="left", padx=10)
        tech.pack_propagate(False)

        ctk.CTkLabel(
            tech,
            text="⚙️ Technologies Used",
            font=("Segoe UI", 18, "bold"),
            text_color="#4CC9F0"
        ).pack(anchor="w", padx=20, pady=(15, 10))

        technologies = [
            "Python",
            "CustomTkinter",
            "Pandas",
            "NumPy",
            "Scikit-learn",
            "Matplotlib"
        ]

        for item in technologies:
            ctk.CTkLabel(
                tech,
                text=f"✔ {item}",
                font=("Segoe UI", 13)
            ).pack(anchor="w", padx=25, pady=2)

        models = ctk.CTkFrame(
            row2,
            corner_radius=15,
            fg_color="#2B2B2B"
        )
        models.pack(side="left", fill="both", expand=True, padx=10)

        ctk.CTkLabel(
            models,
            text="🤖 Machine Learning Models",
            font=("Segoe UI", 18, "bold"),
            text_color="#4CC9F0"
        ).pack(anchor="w", padx=20, pady=(15, 10))

        ctk.CTkLabel(
            models,
            text=(
                "✔ Isolation Forest\n\n"
                "• Detects anomalous cashier transactions.\n\n"
                "✔ Random Forest\n\n"
                "• Identifies suspicious online transactions\n"
                "using supervised learning."
            ),
            justify="left",
            font=("Segoe UI", 13)
        ).pack(anchor="w", padx=20)
        # =====================================================
        # ROW 3 - FEATURES
        # =====================================================

        features = ctk.CTkFrame(
            body,
            corner_radius=15,
            fg_color="#2B2B2B"
        )
        features.pack(fill="x", padx=10, pady=10)

        ctk.CTkLabel(
            features,
            text="✨ Key Features",
            font=("Segoe UI", 18, "bold"),
            text_color="#4CC9F0"
        ).pack(anchor="w", padx=20, pady=(15, 10))

        feature_list = [
            "AI-Powered Cashier Fraud Detection",
            "Online Transaction Fraud Detection",
            "Real-Time Transaction Search",
            "Detailed Fraud Reports",
            "Interactive Graph Analytics",
            "Professional Dashboard",
            "Machine Learning Insights"
        ]

        for feature in feature_list:
            ctk.CTkLabel(
                features,
                text=f"✓ {feature}",
                font=("Segoe UI", 13)
            ).pack(anchor="w", padx=25, pady=3)

        # =====================================================
        # ROW 4 - FUTURE SCOPE
        # =====================================================

        future = ctk.CTkFrame(
            body,
            corner_radius=15,
            fg_color="#2B2B2B"
        )
        future.pack(fill="x", padx=10, pady=10)

        ctk.CTkLabel(
            future,
            text="🚀 Future Scope",
            font=("Segoe UI", 18, "bold"),
            text_color="#4CC9F0"
        ).pack(anchor="w", padx=20, pady=(15, 10))

        future_points = [
            "Database Integration",
            "Cloud Deployment",
            "Live Transaction Monitoring",
            "Explainable AI (XAI)",
            "PDF & Excel Report Export",
            "Email Alert Notifications",
            "Multi-Branch Fraud Monitoring"
        ]

        for item in future_points:
            ctk.CTkLabel(
                future,
                text=f"• {item}",
                font=("Segoe UI", 13)
            ).pack(anchor="w", padx=25, pady=2)

        # =====================================================
        # PROJECT HIGHLIGHTS
        # =====================================================

        highlight = ctk.CTkFrame(
            body,
            corner_radius=15,
            fg_color="#203A43"
        )
        highlight.pack(fill="x", padx=10, pady=15)

        ctk.CTkLabel(
            highlight,
            text="🏆 Project Highlights",
            font=("Segoe UI", 18, "bold"),
            text_color="#7DD3FC"
        ).pack(pady=(15, 10))

        ctk.CTkLabel(
            highlight,
            text=(
                "• Dual Machine Learning Models\n"
                "• Professional Desktop Interface\n"
                "• Intelligent Fraud Analytics\n"
                "• Fast Transaction Search\n"
                "• Interactive Reports & Graphs\n"
                "• Built using Python & CustomTkinter"
            ),
            justify="center",
            font=("Segoe UI", 13)
        ).pack(pady=(0, 15))

        # =====================================================
        # FOOTER
        # =====================================================

        footer = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        footer.pack(fill="x", pady=(10, 20))

        ctk.CTkLabel(
            footer,
            text="────────────────────────────────────────────────────────",
            text_color="#555555"
        ).pack()

        ctk.CTkLabel(
            footer,
            text="🛡️ Cashier Shield AI",
            font=("Segoe UI", 16, "bold"),
            text_color="#4CC9F0"
        ).pack(pady=(10, 2))

        ctk.CTkLabel(
            footer,
            text="AI Powered Fraud Detection System",
            font=("Segoe UI", 12),
            text_color="lightgray"
        ).pack()

        ctk.CTkLabel(
            footer,
            text="© 2026 Shubhashree Bhat | Version 1.0",
            font=("Segoe UI", 11),
            text_color="#8A8A8A"
        ).pack(pady=(5, 0))