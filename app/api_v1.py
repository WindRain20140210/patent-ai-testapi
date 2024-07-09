from flask import Blueprint, jsonify

api_v1 = Blueprint('api_v1', __name__)

@api_v1.route('/')
def hello_world():
    return 'Hello, World!'

@api_v1.route('/v1/getPatensInfo')
def resource1():
    return jsonify([{"time":"2019","val":"300"},{"time":"2020","val":"400"},{"time":"2021","val":"500"},{"time":"2022","val":"600"}])