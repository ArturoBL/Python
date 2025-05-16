from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    #host 0.0.0.0 to allow external connections
    app.run(host='0.0.0.0', port=4030, debug=True)      