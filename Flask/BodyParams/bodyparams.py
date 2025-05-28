from flask import request, Flask

app = Flask(__name__)

# Receive param from body
# test from command line: curl -X POST http://localhost:5000/CreateUser -H "Content-Type: application/json" -d "{\"Username\":\"Arturo\"}"
@app.route('/CreateUser', methods=['POST'])
def crear_usuario():
    data = request.json
    nombre = data.get('Username')
    return f"User created: {nombre}"

if __name__ == '__main__':
    app.run(debug=True)