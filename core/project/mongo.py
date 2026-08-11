from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["travel_db"]

users_collection = db["signup"]
booking_collection = db["bookings"]
contact_collection = db["contactus"]
admin_collection = db["admin"]

