from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from code1.models.store import StoreModel

class Stores(Resource):
    def get(self):
        return {'stores': [x.json() for x in StoreModel.query.all()]}


class Store(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float,
                        required=True,
                        help="This field cannot be left blank."
                        )

    @jwt_required()
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store does not exist'}, 404


    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message':'A store with this name already exists.'}, 400

        store = StoreModel(name)
        store.save_to_db()

        return store.json(), 201


    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'message': 'Store removed.'}


