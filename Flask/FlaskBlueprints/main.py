from flask import Flask
from blueprints.hello.hello import hello_bp
from blueprints.hello2.hello2 import hello2_bp

app = Flask(__name__)

app.register_blueprint(hello_bp)
app.register_blueprint(hello2_bp)

#Welcome route
@app.route("/")
def root():
    return "<html><body><h1>Welcome to API server</h1></body></html>"

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 2020, debug=True)