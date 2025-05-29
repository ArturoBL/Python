import requests

url = 'http://localhost:4030/'  # Consider your actual server's URL
token = 'My$SecretToken'

headers = {
    'Authorization': f'Bearer {token}'
}

# In case you want to send data
payload = {
    'example': 'data'
}

# Realizar la solicitud POST
response = requests.post(url, headers=headers, json=payload)

# Imprimir la respuesta
print(f"Status code: {response.status_code}")
print("Response body:", response.text)