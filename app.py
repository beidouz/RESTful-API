from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from model.monkey import MonkeyModel
from utils.config import host_ip
from utils.error_utils import ErrorUtil
from utils.validator import Validator
from voluptuous.error import MultipleInvalid



app = Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument('monkey_name')


#monkey
#shows a single monkey and lets you delete a single monkey

class Monkey(Resource):

    def get(self, monkey_id):
        print("get a monkey", monkey_id)

        try:
            id_json = {'id': monkey_id}
            Validator.validate_get(id_json)
        except MultipleInvalid as e:
            return ErrorUtil.bad_request(e)
            
        try:
            monkey_entity =MonkeyModel.find_by_id(monkey_id)
        except Exception:
            return ErrorUtil.internal_error(e)

        if not monkey_entity:
            return ErrorUtil.not_found(monkey_id)

        data = jsonify(monkey_entity.__dict__)
        data.status_code = 200
        return data


    def put(self, monkey_id):
        print('put a monkey')
        args = parser.parse_args()

        try:
            updated_monkey = MonkeyModel.update_monkey(monkey_id, args)
        except Exception as e:
            return ErrorUtil.internal_error(e)

        if not updated_monkey:
            return ErrorUtil.not_found(monkey_id)

        data = jsonify(updated_monkey.__dict__)
        data.status_code = 200
        return data


    def delete(self, monkey_id):
        print('delete a monkey')
        try:
            response = MonkeyModel.delete_monkey(monkey_id)
        except Exception as e:
            return ErrorUtil.internal_error(e)

        if not response:
            return ErrorUtil.not_found(monkey_id)

        data = jsonify(response)
        data.status_code = 200
        return data



#  #monkeys
#  #shows a list of monkeys and lets you get all monkeys and POST to add new monkeys
class Monkeys(Resource):

    def get(self):
        print('getting all the monkeys')
        try:
            all_monkeys = MonkeyModel.get_all_monkeys()
        except Exception as e:
            return ErrorUtil.internal_error(e)

        if not all_monkeys:
            return ErrorUtil.not_found()

        data = jsonify(all_monkeys)#__dict__
        data.status_code = 200
        return all_monkeys


    def post(self):
        print('posting a monkey')
        args = parser.parse_args()

        try:
            new_monkey_entity = MonkeyModel.create_monkey(args)
        except Exception as e:
            return ErrorUtil.internal_error(e)


        data = jsonify(new_monkey_entity.__dict__)
        data.status_code = 201
        return data



api.add_resource(Monkeys, '/zoo/monkeys')
api.add_resource(Monkey, '/zoo/monkeys/<string:monkey_id>')

if __name__ == "__main__":
    app.run(host=host_ip, port=5000, debug=True)
