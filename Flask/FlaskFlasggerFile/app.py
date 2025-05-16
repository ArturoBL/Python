from flask import Flask, jsonify, request
from flasgger import Swagger, swag_from

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/suma', methods=['GET'])
@swag_from('docs/suma.yml')     # /apidocs for documentation
def sumar():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    resultado = a + b
    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=True)
