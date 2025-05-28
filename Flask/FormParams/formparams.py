from flask import Flask, request

app = Flask(__name__)

# Get params from form data
# test from command line: curl -X POST http://localhost:5000/login -d "user=admin&Password=1234"
# Or test from form 
'''
<form action="http://localhost:5000/login" method="post">
  <input type="text" name="user">
  <input type="password" name="password">
  <button type="submit">Ingresar</button>
</form>
'''
@app.route('/login', methods=['POST'])
def login():
    usuario = request.form.get('user')
    password = request.form.get('password')
    return f"Login: {usuario}"

if __name__ == '__main__':
    app.run(debug=True)