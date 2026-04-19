from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # MongoDB connection setup
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32117
        DB = 'AAC'
        COL = 'animals'

        # Connect to the database
        self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}')
        self.database = self.client[DB]
        self.collection = self.database[COL]

        # Inserts a new document into the MongoDB collection
    def create(self, data):
        """Insert document into MongoDB. Returns True if successful."""
        if data:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print(f"Create Error: {e}")
                return False
        else:
            raise Exception("Data is empty. Nothing to insert.")

         # Reads and returns documents from MongoDB that match the query
    def read(self, query):
        """Read documents from MongoDB. Returns a list of matches."""
        try:
            return list(self.collection.find(query))
        except Exception as e:
            print(f"Read Error: {e}")
            return []
        
         # Update method
    def update(self, query, new_values):
        try:
            result = self.collection.update_many(query, {"$set": new_values})
            return result.modified_count
        except Exception as e:
            print(f"Update Error: {e}")
            return 0

        # Delete method
    def delete(self, query):
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print(f"Delete Error: {e}")
            return 0