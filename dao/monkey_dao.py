import pymongo
from pymongo import MongoClient
from pymongo.database import ObjectId



class MonkeyDao:
    def get_monkey_by_id(self, monkey_id):

        db_name = "zoo"
        collection_name = "monkeys"
     
        host = "mongo"
        #  host = None
        client = MongoClient(host)
        db = client[db_name]
        collection = db[collection_name]

        a_monkey = collection.find_one({"_id": ObjectId(monkey_id)})
        
        return a_monkey


