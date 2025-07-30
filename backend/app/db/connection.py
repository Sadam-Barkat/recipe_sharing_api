# backend/db/connection.py

from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get MongoDB connection details
MONGODB_URI = os.getenv("MONGODB_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")

# Create MongoDB client and connect to the database
client = MongoClient(MONGODB_URI)
db = client[DATABASE_NAME]

# Access the "recipes" collection
recipe_collection = db["recipes"]
