from flask import jsonify


def index():
    return jsonify({'message': 'holis'})
