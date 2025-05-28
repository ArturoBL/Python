from flask import request, Flask

app = Flask(__name__)

# Get query params
# http://127.0.0.1:5000/Search?Username=rootuser
@app.route('/Search')
def Search():
    Username = request.args.get('Username', '')  # valor por defecto vacío
    return f"Searching for: {Username}"

if __name__ == '__main__':
    app.run(debug=True)