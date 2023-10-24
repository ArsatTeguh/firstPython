from pymongo import MongoClient
client = MongoClient()
db = client["articles"]
connection = db["article_db"]
