from flask import Blueprint, jsonify

api_v2 = Blueprint('api_v2', __name__)

@api_v2.route('/v2/resource1')
def resource1():
    return jsonify({'message': 'This is resource 1 from API v2'})

@api_v2.route('/v2/resource2')
def resource2():
    return jsonify({'message': 'This is resource 2 from API v2'})
