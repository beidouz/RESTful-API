from dao.monkey_dao import MonkeyDao



class MonkeyModel:
    def __init__(self, collection):
        #constructor
        self.monkey_id = str(collection['_id'])
        self.monkey_name = str(collection['monkey_name'])
        

    @staticmethod
    def find_by_id(monkey_id):
        dao = MonkeyDao() 
        monkey_data = dao.get_monkey_by_id(monkey_id)
        monkey_model = None

        if monkey_data:
            monkey_model = MonkeyModel(monkey_data)

        return monkey_model
    

    @staticmethod 
    def create_monkey(monkey_info):
        dao = MonkeyDao()
        new_monkey_data = dao.make_monkey(monkey_info)
        new_monkey_model = None
        
        if new_monkey_data:
            new_monkey_model = MonkeyModel(new_monkey_data)
        
        return new_monkey_model

