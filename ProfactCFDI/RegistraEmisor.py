import os
import base64

# Instalar biblioteca zeep -> pip install zeep
from zeep import Client

def file_to_base64(archivo):
    # Obtiene la ruta del directorio donde se ejecuta el script actual
    dir_path = os.path.dirname(os.path.realpath(__file__))
    
    # Une el directorio con el nombre del archivo XML
    file_path = os.path.join(dir_path, 'ArchivosPrueba\IIA040805DZ4', archivo)

    # Lee el archivo XML
    with open(file_path, 'rb') as _archivo:
        contenido = _archivo.read()

    # Convierte el contenido del XML a base64
    base64_content = base64.b64encode(contenido)

    # Retorna la cadena base64
    return base64_content

# Define la URL del WSDL
wsdl_url = 'https://pruebas.timbracfdi33.mx/Timbrado.asmx?wsdl'

# Crea el cliente
client = Client(wsdl_url)

# Define los parámetros para la función TimbraCFDI

#Usuario integrador pruebas -> mvpNUXmQfK8=
usuarioIntegrador = 'mvpNUXmQfK8='
#RFC Emisor
rfcEmisor = 'IIA040805DZ4'
#Archivo .cer en base64
archivoCer = 'publicCer.cer'
base64Cer = file_to_base64(archivoCer)
#Archivo .key en base64
archivoKey = 'privateKey.key'
base64Key = file_to_base64(archivoKey)
#Contrasena de llave privada
contrasena = '12345678a'

# Usa la función TimbraCFDI
response = client.service.RegistraEmisor(usuarioIntegrador, rfcEmisor, base64Cer, base64Key, contrasena)
tipoExepcion, codigoError, descripcion, Pos4, Pos5, Pos6, codigoInterno, descripcionInterna, Detalle = response

print(tipoExepcion)
print(codigoError)
print(descripcion)
print(codigoInterno)
print(descripcionInterna)
print(Detalle)

# Revisa la Guía de integración para conocer más sobre los parámetros de petición y respuesta -> https://profact.com.mx/wp-content/uploads/2023/06/GuiaWSTimbraCFDI.zip
