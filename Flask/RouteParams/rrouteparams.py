from flask import Flask

app = Flask(__name__)

# Get Username from the route
# Test with: http://127.0.0.1:5000/User/rootuser
@app.route('/User/<string:UserName>')
def get_usuario(UserName):
    return f"Your username is: {UserName}"

if __name__ == '__main__':
    app.run(debug=True)