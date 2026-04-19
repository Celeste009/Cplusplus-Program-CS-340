from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # MongoDB connection setup
        USER = username
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32117
        DB = 'AAC'
        COL = 'animals'

        # Connect to the database
        self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}')
        self.database = self.client[DB]
        self.collection = self.database[COL]

        # ✅ Indexing for performance
        self.collection.create_index("breed")
        self.collection.create_index("animal_type")

    # CREATE
    def create(self, data):
        """Insert document into MongoDB. Returns True if successful."""
        if data:
            try:
                # ✅ Basic validation
                if "name" not in data or "animal_type" not in data:
                    raise Exception("Missing required fields")

                self.collection.insert_one(data)
                return True
            except Exception as e:
                print(f"Create Error: {e}")
                return False
        else:
            raise Exception("Data is empty. Nothing to insert.")

    # READ
    def read(self, query):
        """Read documents from MongoDB. Returns a list of matches."""
        try:
            return list(self.collection.find(query))
        except Exception as e:
            print(f"Read Error: {e}")
            return []

    # UPDATE
    def update(self, query, new_values):
        try:
            result = self.collection.update_many(query, {"$set": new_values})
            return result.modified_count
        except Exception as e:
            print(f"Update Error: {e}")
            return 0

    # DELETE
    def delete(self, query):
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print(f"Delete Error: {e}")
            return 0

    # ✅ NEW: Aggregation Pipeline (Milestone 4 requirement)
    def aggregate_animals(self, pipeline):
        """Perform advanced MongoDB aggregation queries."""
        try:
            return list(self.collection.aggregate(pipeline))
        except Exception as e:
            print(f"Aggregation Error: {e}")
            return []