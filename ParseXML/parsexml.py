import xml.etree.ElementTree as ET

# Cargar y parsear el archivo XML
tree = ET.parse('ejemplo.xml')
root = tree.getroot()

# Recorrer los elementos del catálogo
for libro in root.findall('libro'):
    id_libro = libro.get('id')
    titulo = libro.find('titulo').text
    autor = libro.find('autor').text
    precio = libro.find('precio').text

    print(f"ID: {id_libro}")
    print(f"Título: {titulo}")
    print(f"Autor: {autor}")
    print(f"Precio: ${precio}")
    print("-------------")
