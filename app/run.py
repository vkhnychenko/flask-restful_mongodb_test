from bson import ObjectId
from bson.json_util import _json_convert
from flask import Flask
from flask_restful import Resource, Api, reqparse, abort
from flask_pymongo import PyMongo
from settings import MONGO_URI
from errors_handler import APIException

app = Flask(__name__)
app.config["MONGO_URI"] = MONGO_URI
mongo = PyMongo(app)
api = Api(app, prefix='/api')


class GetItem(Resource):
    def get(self, id):
        try:
            item = mongo.db.item.find_one({"_id": ObjectId(id)}, {"_id": 0})
            resp = _json_convert(item)
            return {'name': resp['name']}, 200
        except APIException as e:
            abort(e.code, str(e))


class CreateItem(Resource):
    def post(self):
        try:
            params = parser.parse_args()
            result = mongo.db.item.insert_one({'name': params['name']})
            return {"id": _json_convert(result.inserted_id)}, 201
        except APIException as e:
            abort(e.code, str(e))


parser = reqparse.RequestParser()
parser.add_argument("name", location='form')
api.add_resource(CreateItem, '/item/create')
api.add_resource(GetItem, '/item/<id>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)