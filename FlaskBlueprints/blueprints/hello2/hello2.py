from flask import Blueprint

hello2_bp = Blueprint('hello2', __name__)

@hello2_bp.route('/hello2', methods=['GET'])
def hello2():
    return '<h2>This is second hello api</h2>'