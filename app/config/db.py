
from pymongo import MongoClient
import os


password = os.environ.get("MONGODB_PWD")
from app.models.user import Program
conn = MongoClient(f"mongodb+srv://ayoubtaouabi6:{password}@cluster0.s4ulmp6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = conn["production"]  # Replace "your_database" with your actual database name
user = db["user"]


# # Delete all documents in the collection
# result = user.delete_many({})
# # Print the number of documents deleted
# print(f"{result.deleted_count} documents deleted.")
