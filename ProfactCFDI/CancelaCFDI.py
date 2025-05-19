import os
import base64

# Instalar biblioteca zeep -> pip install zeep
from zeep import Client

# Define la URL del WSDL
wsdl_url = 'https://pruebas.timbracfdi33.mx/Timbrado.asmx?wsdl'

# Crea el cliente
client = Client(wsdl_url)

# Define los parámetros para la función TimbraCFDI

#Usuario integrador pruebas -> mvpNUXmQfK8=
usuarioIntegrador = 'mvpNUXmQfK8='
#RFC Emisor
rfcEmisor = 'IIA040805DZ4'
#Folio Fiscal
folioUUID = 'df454f00-8b9c-4135-b8b2-7780ad3d83f0'
#Motivo de cancelación
motivoCancelacion = '03'
#Folio Fiscal de sustitución
folioUUIDSustitucion = '' # Aplica para motivo de cancelación 01

# Usa la función CancelaCFDI
response = client.service.CancelaCFDI40(usuarioIntegrador, rfcEmisor, folioUUID, motivoCancelacion, folioUUIDSustitucion)
tipoExepcion, codigoError, descripcion, Pos4, Pos5, Pos6, codigoInterno, descripcionInterna, Detalle = response

print(tipoExepcion)
print(codigoError)
print(descripcion)
print(codigoInterno)
print(descripcionInterna)
print(Detalle)

# Revisa la Guía de integración para conocer más sobre los parámetros de petición y respuesta -> https://profact.com.mx/wp-content/uploads/2023/06/GuiaWSTimbraCFDI.zip
