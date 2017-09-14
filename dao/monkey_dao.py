import pymongo
from pymongo import MongoClient
from pymongo.database import ObjectId


#host_name = None
host_name = 'mongo'
db_name = 'zoo'
collection_name = 'monkeys'


class MonkeyDao:
    
    def __init__(self):
        self.connection = MongoClient(host_name)
        self.db = self.connection[db_name]
        self.collection = self.db[collection_name]# pointer to the collection? not the actual collection data


    def get_monkey_by_id(self, monkey_id):
        a_monkey = self.collection.find_one({"_id": ObjectId(monkey_id)}) 
        return a_monkey
    
    
    def get_monkey_collection(self):
        return self.collection


    def make_monkey(self, monkey_info):
        new_collection = self.collection.insert_one(monkey_info)
        #new monkey inserted into collection
        #unique id for new monkey automatically generated
        new_monkey_data = self.collection.find_one({"_id":new_collection.inserted_id})
        return new_monkey_data


