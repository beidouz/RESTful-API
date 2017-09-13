
from dao.monkey_dao import MonkeyDao



class MonkeyModel:
    def __init__(self, collection):
        #constructor
        self.monkey_id = str(collection['_id'])
        self.monkey_name = str(collection['monkey_name'])
        

    @staticmethod
    def find_by_id(monkey_id):
        dao = MonkeyDao() 
        monkey = dao.get_monkey_by_id(monkey_id)
        monkey_model = None

        if monkey:
            monkey_model = MonkeyModel(monkey)

        return monkey_model

