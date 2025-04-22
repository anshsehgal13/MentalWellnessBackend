import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from dotenv import load_dotenv

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise ValueError("❌ MONGO_URI not found in environment variables.")

try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    server_info = client.server_info()
    print("✅ Successfully connected to MongoDB!")
    print("🖥️ MongoDB Server Info:", server_info.get("version"))

    db = client["mentalhealth"]
    posts_collection = db["vent_posts"]
    scores_collection = db["user_scores"]

except ConnectionFailure as e:
    print("❌ MongoDB connection failed.")
    print("Error:", e)
    raise
