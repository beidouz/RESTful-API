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


    def find_by_id(self, monkey_id):
        a_monkey = self.collection.find_one({"_id": ObjectId(monkey_id)}) 
        return a_monkey
    
    
    def get_all_monkeys(self):
        return self.collection


    def create_monkey(self, monkey_info):
        new_collection = self.collection.insert_one(monkey_info)
        #new monkey inserted into collection
        #unique id for new monkey automatically generated
        new_monkey_data = self.collection.find_one({"_id":new_collection.inserted_id})
        return new_monkey_data


    def update_monkey(self, monkey_id, monkey_info):
        update_monkey_data = self.collection.update_one({"_id": ObjectId(monkey_id)}, {"$set": monkey_info})
        updated_monkey_data = self.collection.find_one({"_id": ObjectId(monkey_id)})
        return updated_monkey_data        



    def delete_monkey(self, monkey_id):
        a_monkey = self.collection.find_one({"_id": ObjectId(monkey_id)})
        #if monkey doesn't exist in the collection -> do nothing
        if not a_monkey:
            return None
        else:
            deleted_collection = self.collection.delete_one({"_id": ObjectId(monkey_id)})
            return deleted_collection



