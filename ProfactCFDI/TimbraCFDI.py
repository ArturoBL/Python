import os
import base64

# Instalar biblioteca zeep -> pip install zeep
from zeep import Client

def xml_to_base64(archivo_xml):
    # Obtiene la ruta del directorio donde se ejecuta el script actual
    dir_path = os.path.dirname(os.path.realpath(__file__))
    
    # Une el directorio con el nombre del archivo XML
    xml_path = os.path.join(dir_path, 'ArchivosPrueba\Ejemplos CFDIv40', archivo_xml)

    # Lee el archivo XML
    with open(xml_path, 'rb') as xml_file:
        xml_content = xml_file.read()

    # Convierte el contenido del XML a base64
    base64_content = base64.b64encode(xml_content)

    # Retorna la cadena base64
    return base64_content.decode('utf-8')

# Define la URL del WSDL
wsdl_url = 'https://pruebas.timbracfdi33.mx/Timbrado.asmx?wsdl'

# Crea el cliente
client = Client(wsdl_url)

# Define los parámetros para la función TimbraCFDI

#Usuario integrador pruebas -> mvpNUXmQfK8=
usuarioIntegrador = 'mvpNUXmQfK8='
#Xml a timbrar codificado en base64
archivo_xml = 'CFDIv4_Ingreso.xml'
xmlComprobanteBase64 = xml_to_base64(archivo_xml)

#IdComprobante
idComprobante = 'ABC123'

# Usa la función TimbraCFDI
response = client.service.TimbraCFDI(usuarioIntegrador, xmlComprobanteBase64, idComprobante)
tipoExepcion, codigoError, descripcion, Xml, QR, CadenaOriginal, codigoInterno, descripcionInterna, Detalle = response

print(tipoExepcion)
print(codigoError)
print(descripcion)
print(Xml)
print(QR)
print(CadenaOriginal)
print(codigoInterno)
print(descripcionInterna)
print(Detalle)

print(os.getcwd())

# Ejemplo para guardar imagen QR como archivo (misma ruta del archivo TimbraCFDI.py)

# Obtener la ruta del script en ejecución
script_directory = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta completa para el archivo de salida
output_path = os.path.join(script_directory, "QR.jpeg")

# Guardar la imagen en la ruta especificada
with open(output_path, "wb") as f:
    f.write(QR)
    
# Ejemplo para convertir QR en base64
base64_image = base64.b64encode(QR).decode("utf-8")
print(base64_image)

# Revisa la Guía de integración para conocer más sobre los parámetros de petición y respuesta -> https://profact.com.mx/wp-content/uploads/2023/06/GuiaWSTimbraCFDI.zip
