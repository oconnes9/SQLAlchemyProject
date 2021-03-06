from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity

from code1.resources.user import UserRegister
from code1.resources.item import Item, Items
from code1.resources.store import Store, Stores

from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
app.secret_key = 'Sean'

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)  #/auth endpoint created

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(Stores, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
