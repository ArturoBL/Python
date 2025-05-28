from flask import Flask, request, jsonify

app = Flask(__name__)

# Get params from header
# Test from command line: curl -X POST http://localhost:5000/data_processing  -H "Content-Type: application/json" -H "X-API-Key: abc123" -H "X-Cliente-ID: cliente_456" -d "{\"name\": \"Arturo\", \"age\": 35}"
@app.route('/data_processing', methods=['POST'])
def procesar_datos():
    # Obtener parámetros del header
    api_key = request.headers.get('X-API-Key')
    cliente_id = request.headers.get('X-Cliente-ID')

    # Obtener datos del cuerpo JSON
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')

    return jsonify({
        'api_key': api_key,
        'cliente_id': cliente_id,
        'name': name,
        'age': age
    })

if __name__ == '__main__':
    app.run(debug=True)