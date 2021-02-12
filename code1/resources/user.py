from flask_restful import Resource, reqparse
from code1.models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str,
                        required=True,
                        help="This field cannot be left blank."
                        )
    parser.add_argument('password', type=str,
                        required=True,
                        help="This field cannot be left blank."
                        )

    def post(self):
        data = self.parser.parse_args()
        user = UserModel.find_by_username(data['username'])

        if user:
            return {"message":'Username already exists.'}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully."}, 201