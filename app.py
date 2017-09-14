from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from model.monkey import MonkeyModel


app = Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument('monkey_name')


#monkey
#shows a single monkey and lets you delete a single monkey
   
class Monkey(Resource):
    
    def get(self, monkey_id):
        print("get a monkey", monkey_id)
        monkey_entity = MonkeyModel.find_by_id(monkey_id)
        if monkey_entity:
            data = jsonify(monkey_entity.__dict__)
        else:
            data = "Monkey trying to get does not exist"
        return data
  
    
    def put(self, monkey_id):
        print('put a monkey')
        args = parser.parse_args()
        updated_monkey = MonkeyModel.update_monkey(monkey_id, args)
        if updated_monkey:  
            data = jsonify(updated_monkey.__dict__)
        else:
            data = "Monkey trying to put does not exist"
        return data
    
    
    def delete(self, monkey_id):
        print('delete a monkey')
        response = MonkeyModel.delete_monkey(monkey_id)
        data = jsonify(response)
        return data



#  #monkeys
#  #shows a list of monkeys and lets you get all monkeys and POST to add new monkeys
class Monkeys(Resource):
     
    def get(self):
        print('getting all the monkeys')
        all_monkeys = MonkeyModel.get_all_monkeys()
        #  data = jsonify(all_monkeys.__dict__) 
        return all_monkeys
    
    
    def post(self):
        print('posting a monkey')
        args = parser.parse_args()
        # parse_args()  Vs.  request.get_json()      which one should I use?
        new_monkey_entity = MonkeyModel.create_monkey(args)
        data = jsonify(new_monkey_entity.__dict__)
        return data



api.add_resource(Monkeys, '/zoo/monkeys')
api.add_resource(Monkey, '/zoo/monkeys/<string:monkey_id>') 

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
