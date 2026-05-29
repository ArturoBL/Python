import requests
import time

BASE_URL = "http://localhost:8000"

def print_test(name):
    print(f"\n{'='*20} {name} {'='*20}\n")


#1. Login con usuario admin
print_test("Prueba 1. Login con usuario admin")
response = requests.post(f"{BASE_URL}/token", data={"username": "admin", "password": "admin123"})
if response.status_code == 200:
    token = response.json().get("access_token")
    print("Token obtenido:", token)
    headers = {"Authorization": f"Bearer {token}"}
    admin_response = requests.get(f"{BASE_URL}/admin", headers=headers)
    print("Status:", admin_response.status_code)
    print("Respuesta del endpoint /admin:", admin_response.json())
    print("Token obtenido:", token)
else:
    print("Error al obtener token:", response.status_code, response.text)

#2. Login con usuario no existente
print_test("Prueba 2. Login con usuario no existente")
response = requests.post(f"{BASE_URL}/token", data={"username": "nonexistent", "password": "wrongpass"})
print("Status:", response.status_code)
print("Respuesta:", response.json())

#3. Login con usuario admin pero contraseña incorrecta
print_test("Prueba 3. Login con usuario admin pero contraseña incorrecta")
response = requests.post(f"{BASE_URL}/token", data={"username": "admin", "password": "wrongpass"})
print("Status:", response.status_code)
print("Respuesta:", response.json())

#4. Acceso al endpoint /admin sin token
print_test("Prueba 4. Acceso al endpoint /admin sin token")
admin_response = requests.get(f"{BASE_URL}/admin")
print("Status:", admin_response.status_code)
print("Respuesta:", admin_response.json())

#5. Acceso al endpoint /admin con usuario no admin
print_test("Prueba 5. Acceso al endpoint /admin con usuario no admin")
response = requests.post(f"{BASE_URL}/token", data={"username": "user", "password": "user123"})
if response.status_code == 200:
    token = response.json().get("access_token")
    print("Token obtenido:", token)
    headers = {"Authorization": f"Bearer {token}"}
    admin_response = requests.get(f"{BASE_URL}/admin", headers=headers)
    print("Status:", admin_response.status_code)
    print("Respuesta del endpoint /admin:", admin_response.json())

#6. Acceso al endpoint /admin con token inválido
print_test("Prueba 6. Acceso al endpoint /admin con token inválido")
headers = {"Authorization": "Bearer eyJ.invalid.token"}
admin_response = requests.get(f"{BASE_URL}/admin", headers=headers)
print("Status:", admin_response.status_code)
print("Respuesta:", admin_response.json())