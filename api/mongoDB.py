# ------------------------------- #
#            Rest API             #
#     with MongoDB as database    #
# ------------------------------- #
import os

from pymongo import MongoClient


# Get MongoDB Database
def get_database():
    # Configure
    user_name = os.getenv("MONGODB_USER_NAME")
    password = os.getenv("MONGODB_PASSWORD")
    dbname = os.getenv("MONGODB_DBNAME")

    # Connect to MongnDB
    CONNECTION_STRING = f"mongodb+srv://{user_name}:{password}@mern.vzfjptn.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    print(f"Successfully connected to Mongodb database '{dbname}'!")

    return client[dbname]


# Check Items


# Add Items
def add_items(database):
    # Get the database
    collection = database["Items"]
    item_1 = {
        "_id": "U1IT00005",
        "item_name": "Blender",
        "max_discount": "10%",
        "batch_number": "RR450020FRG",
        "price": 340,
        "category": "kitchen appliance",
    }
    item_2 = {
        "_id": "U1IT00006",
        "item_name": "Egg",
        "category": "food",
        "quantity": 12,
        "price": 36,
        "item_description": "brown country eggs",
    }
    value = collection.insert_many([item_1, item_2])
    print(value)
    return {"value": "value"}


# Delete Items


# Update Items


# Create Collection
def create_collection():
    pass


# if __name__ == "__main__":
#     get_database()
