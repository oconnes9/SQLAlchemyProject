from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from code1.models.item import ItemModel

class Items(Resource):
    def get(self):
        return {'items': [x.json() for x in ItemModel.query.all()]}


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float,
                        required=True,
                        help="This field cannot be left blank."
                        )
    parser.add_argument('store_id', type=int,
                        required=True,
                        help="Every item needs a store id."
                        )
    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item does not exist'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message':'An item with this name already exists.'}, 400

        request_data = self.parser.parse_args()
        item = ItemModel(name, request_data['price'], request_data['store_id'])

        item.save_to_db()

        return item.json(), 201

    def put(self, name):
        request_data = self.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item:
            item.price = request_data['price']
            item.price = request_data['store_id']

        else:
            item = ItemModel(name, request_data['price'], request_data['store_id'])

        item.save_to_db()
        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message':'Item removed.'}

        return {'Error': None}, 404  # 404 is not found

