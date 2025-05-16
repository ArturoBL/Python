import json

# Abrimos el archivo en modo lectura
with open('datos.json', 'r', encoding='utf-8') as archivo:
    datos = json.load(archivo)  # Parseamos el contenido del JSON a un diccionario

# Mostramos los datos
print(datos)
print("Nombre:", datos["nombre"])
print("Lenguajes:", ", ".join(datos["lenguajes"]))
