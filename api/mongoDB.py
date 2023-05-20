# ------------------------------- #
#            Rest API             #
#     with MongoDB as databse     #
# ------------------------------- #
from pymongo import MongoClient


# Get MongoDB Database
def get_database():
    # Configure
    user_name = ""
    password = ""
    dbname = ""

    # Connect to MongnDB
    CONNECTION_STRING = f"mongodb+srv://{user_name}:{password}@mern.vzfjptn.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)

    return client[dbname]


# Insert Items
def add_items():
    # Get the database
    dbname = get_database()
    collection_name = dbname["Items"]
    item_1 = {
        "_id": "U1IT00001",
        "item_name": "Blender",
        "max_discount": "10%",
        "batch_number": "RR450020FRG",
        "price": 340,
        "category": "kitchen appliance",
    }
    item_2 = {
        "_id": "U1IT00002",
        "item_name": "Egg",
        "category": "food",
        "quantity": 12,
        "price": 36,
        "item_description": "brown country eggs",
    }
    collection_name.insert_many([item_1, item_2])


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":
    get_database()
