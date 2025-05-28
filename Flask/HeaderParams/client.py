import requests

url = 'http://localhost:5000/data_processing'

# Encabezados personalizados
headers = {
    'Content-Type': 'application/json',
    'X-API-Key': 'abc123',
    'X-Cliente-ID': 'cliente_456'
}

# Datos del cuerpo (JSON)
payload = {
    'name': 'Arturo',
    'age': 35
}

# Enviar la solicitud POST
response = requests.post(url, headers=headers, json=payload)

# Mostrar respuesta
print('Status code:', response.status_code)
print('Response:', response.json())
