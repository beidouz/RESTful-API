from dao.monkey_dao import MonkeyDao



class MonkeyModel:
    def __init__(self, collection):
        #constructor
        self.monkey_id = str(collection['_id']) if '_id' in collection else None
        self.monkey_name = str(collection['monkey_name']) if 'monkey_name' in collection else None
#TODO check if the name is valid

    @staticmethod
    def find_by_id(monkey_id):
        dao = MonkeyDao()
        monkey_data = dao.find_by_id(monkey_id)
        monkey_model = None

        if monkey_data:
            monkey_model = MonkeyModel(monkey_data)
        return monkey_model

    @staticmethod
    def get_all_monkeys():
        dao = MonkeyDao()
        monkey_collection = dao.get_all_monkeys()
        all_monkeys = []
        for monkey_data in monkey_collection.find():
            a_monkey = MonkeyModel(monkey_data)
            all_monkeys.append(a_monkey.__dict__)
        return all_monkeys



    @staticmethod
    def create_monkey(monkey_info):
        dao = MonkeyDao()
        new_monkey_data = dao.create_monkey(monkey_info)
        new_monkey_model = None

        if new_monkey_data:
            new_monkey_model = MonkeyModel(new_monkey_data)

        return new_monkey_model



    @staticmethod
    def update_monkey(monkey_id, monkey_info):
        dao = MonkeyDao()
        updated_monkey_data = dao.update_monkey(monkey_id, monkey_info)
        updated_monkey = None
        if updated_monkey_data:
            updated_monkey = MonkeyModel(updated_monkey_data)
        return updated_monkey



    @staticmethod
    def delete_monkey(monkey_id):
        dao = MonkeyDao()
        response = dao.delete_monkey(monkey_id)
        if response:
            response = {'message': 'monkey ' + monkey_id + ' deleted'}
        return response
