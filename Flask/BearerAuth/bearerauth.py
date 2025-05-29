from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)

#predefined token
VALID_TOKEN = "My$SecretToken"

#Require authorization token for any route by a wrapper function
# Test from cmd:curl -X POST http://localhost:4030/ -H "Authorization: Bearer My$SecretToken"

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token or token != f"Bearer {VALID_TOKEN}":
            if token != None:
                tokenreceived = token.split()[1]  # Extract the actual token
                if tokenreceived != VALID_TOKEN:
                    return jsonify({"message": f"Ivalid Token received{tokenreceived}"}), 401
            return jsonify({"message": "Ivalid Token received"}), 401
        return f(*args, **kwargs)
    return decorated

#Wrap the index route requirinf the token
@app.route('/', methods=['POST'])
@token_required
def index():
    return 'Hello, World!, correct token!'

if __name__ == '__main__':
    #host 0.0.0.0 to allow external connections
    app.run(host='0.0.0.0', port=4030, debug=True)      