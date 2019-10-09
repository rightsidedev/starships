from app.api import api
from flask_api import status
from flask import request

id = 1

db = {
        "ships": [
            {
                "id": 1,
                "name": "Enterprise",
                "age": 68
            }
        ]
}

@api.route('/ships/', methods=['GET'])
def get_ships():
    return { "data": db['ships'] }

@api.route('/ships/<int:id>/', methods=['GET'])
def get_ship(id):
    for ship in db['ships']:
        if ship['id'] == id:
            result = ship
            return result
    return {}, status.HTTP_404_NOT_FOUND

@api.route('/ships/<int:id>/', methods=['DELETE'])
def delete_ship(id):
    for ship in db['ships']:
        if ship['id'] == id:
            db['ships'].remove(ship)
            return {},status.HTTP_204_NO_CONTENT
    return {}, status.HTTP_404_NOT_FOUND

@api.route('/ships/', methods=['POST'])
def create_ship():
    data = request.get_json()
    print(data)
    if 'name' in data: # Check the request data has these fields
        if data['name']: # Check they arent none
            global id # BAD! just using a global id
            id += 1
            data['id'] = id
            db['ships'].append(data)
            return data, status.HTTP_201_CREATED
    return {"error":"Must have name property"}, status.HTTP_400_BAD_REQUEST

@api.route('/ships/<int:id>/', methods=['PUT'])
def update_ship(id):
    data = request.get_json()
    print(data)
    for ship in db['ships']:
        if ship['id'] == id:
            if data['name']:
                ship['name'] == data['name']
            if data['age']:
                ship['age'] == data['age']
            return ship, status.HTTP_202_ACCEPTED
    return {}, status.HTTP_404_NOT_FOUND
