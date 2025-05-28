import requests

# URL 
url = 'http://localhost:5000//CreateUser'

# Data to send
payload = {
    'Username': 'Arturo'    
}

# Header
headers = {
    'Content-Type': 'application/json'
}

# Response
response = requests.post(url, json=payload, headers=headers)

# Show response
print('Código de estado:', response.status_code)
print('Respuesta del servidor:', response.text)