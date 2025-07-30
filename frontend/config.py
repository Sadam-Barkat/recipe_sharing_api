# frontend/config.py

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Backend API configuration
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

# API endpoints
RECIPES_ENDPOINT = f"{BACKEND_URL}/recipes"

# App configuration
APP_TITLE = "🍳 Recipe Sharing App"
APP_ICON = "🍳"
PAGE_CONFIG = {
    "page_title": "Recipe Sharing App",
    "page_icon": "🍳",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
} 