import requests

url = 'http://localhost:5000/login'

# Datos como diccionario (se codifican como x-www-form-urlencoded)
form_data = {
    'user': 'admin',
    'password': '1234'
}

# Enviar solicitud POST
response = requests.post(url, data=form_data)

print('Status code:', response.status_code)
print('Response:', response.text)
