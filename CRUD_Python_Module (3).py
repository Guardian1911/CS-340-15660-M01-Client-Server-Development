# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = 'aacuser' 
        PASS = 'SNHU1234'
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    def create(self, data):
        """Insert a document into the animals collection."""

        if data is not None:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print("An error occurred while inserting:", e)
                return False
        else:
            print("Nothing to save because data is empty.")
            return False

    def read(self, data):
        """Read documents from the animals collection."""

        if data is not None:
            try:
                cursor = self.collection.find(data)
                return list(cursor)
            except Exception as e:
                print("An error occurred while reading:", e)
                return []
        else:
            print("Nothing to search because data is empty.")
            return []
        
    def update(self, query, new_values):

        if query is not None and new_values is not None:
            try:
                update_result = self.collection.update_many(
                    query,
                    {"$set": new_values}
                )
                return update_result.modified_count
            except Exception as e:
                print("Error updating documents:", e)
                return 0
        else:
            print("Query or new values are empty.")
            return 0

    def delete(self, query):

        if query is not None:
            try:
                delete_result = self.collection.delete_many(query)
                return delete_result.deleted_count
            except Exception as e:
                print("Error deleting documents:", e)
                return 0
        else:
            print("Nothing to delete because query is empty.")
            return 0