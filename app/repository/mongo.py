import os
from pymongo import MongoClient

COLLECTION_NAME = 'kudos'
class MongoRepository(object):
    def __init__(self):
        print(self)
        mongo_url = os.environ.get('MONGO_URL')
        print(mongo_url)
        self.db = MongoClient(mongo_url).kudos
        print("successfully connect mongodb", self)
    def find_all(self, selector):
        return self.db.kudos.find(selector)
    def find(self, selector):
        return self.db.kudos.find_one(selector)
    def create(self, kudo):
        return self.db.kudos.insert_one(kudo)
    def update(self, selector, kudo):
        return self.db.kudos.replace_one(selector, kudo).modified_count
    def delete(self, selector, kudo):
        return self.db.kudos.delete_one(selector).deleted_count
# from pymongo import MongoClient
# from pymongo.errors import ConnectionFailure
# try:
#     client = MongoClient("mongodb://localhost:27017/")
#     client.admin.command('ping')
#     print("Successfully connected to MongoDB!")
# except ConnectionFailure as e:
#     print(f"Could not connect to MongoDB: {e}")
# finally:
#     client.close()    