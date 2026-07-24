"""
=========================================================
Cashier Shield AI
UI Theme Configuration
=========================================================
"""

import customtkinter as ctk

# -----------------------------
# Appearance
# -----------------------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# -----------------------------
# Window
# -----------------------------

APP_TITLE = "Cashier Shield AI"

WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 800

MIN_WIDTH = 1200
MIN_HEIGHT = 700

# -----------------------------
# Sidebar
# -----------------------------

SIDEBAR_WIDTH = 240

# -----------------------------
# Fonts
# -----------------------------

TITLE_FONT = ("Segoe UI", 28, "bold")
SUBTITLE_FONT = ("Segoe UI", 18)
NORMAL_FONT = ("Segoe UI", 14)
SMALL_FONT = ("Segoe UI", 12)
CARD_FONT = ("Segoe UI", 26, "bold")
CONSOLE_FONT = ("Consolas", 13)

# -----------------------------
# Colors
# -----------------------------

PRIMARY = "#2563EB"
SUCCESS = "#16A34A"
WARNING = "#F59E0B"
DANGER = "#DC2626"
INFO = "#0EA5E9"

BACKGROUND = "#1E1E1E"

CARD_RADIUS = 15
BUTTON_HEIGHT = 42

STATUS_READY = "🟢 Ready"
STATUS_RUNNING = "🟡 Running..."
STATUS_COMPLETED = "✅ Completed"
STATUS_ERROR = "🔴 Error"