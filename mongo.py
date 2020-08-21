import os
import pymongo
if os.path.exists("env.py"):
    import env


# Constant variables to make code cleaner
# Set to the environmet variable from the env.py file
MONGO_URI = os.environ.get("MONGO_URI")
# Set to the name of our DB
DATABASE = "myFirstDB"
# Set to the name of our collection
COLLECTION = "celebrities"


# Create function to try and connect to the DB
def mongo_connect(url):
    # The try block lets you test a block of code for errors
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    # The except block lets you handle the error
    except pymongo.errors.ConnectionFailure as e:
        # This will pring the error string and mongo error in the placeholder
        print("Could not connect to MongoDB: %s") % e


# Call function with the MONGO_URI as the argument
conn = mongo_connect(MONGO_URI)

# Set collection name which will be the connection object and the
# DATABASE and COLLECTION variables
coll = conn[DATABASE][COLLECTION]

# Variable 'documents' will find all items from our celeb DB this will
# return a mongDB object aka a cursor which we need to iterate over in
# order to unpackage it
coll.update_one({"nationality": "american"}, {"$set": {"hair_color": "maroon"}})

documents = coll.find({"nationality": "american"})

for doc in documents:
    print(doc)
