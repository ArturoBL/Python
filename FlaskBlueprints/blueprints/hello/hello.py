from flask import Blueprint

hello_bp = Blueprint('hello', __name__)

@hello_bp.route('/hello', methods=['GET'])
def hello():
    return '<h2>This is hello api<h2>'