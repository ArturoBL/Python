from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)


@app.route('/suma', methods=['GET'])
def sumar():
    #To see documentation go to http://127.0.0.1:5000/apidocs
    """
    Suma dos números
    ---
    parameters:
      - name: a
        in: query
        type: number
        required: true
        description: Primer número a sumar
      - name: b
        in: query
        type: number
        required: true
        description: Segundo número a sumar
    responses:
      200:
        description: Resultado de la suma
        schema:
          type: object
          properties:
            resultado:
              type: number
              example: 8
    """
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    resultado = a + b
    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=True)
