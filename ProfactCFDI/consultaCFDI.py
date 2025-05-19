import xml.etree.ElementTree as ET
from zeep import Client



wsdl_url = 'https://timbracfdi33.mx:1443/Timbrado.asmx?WSDL'

client = Client(wsdl_url)

usuarioIntegrador = 'mvpNUXmQfK8='
UUID = 'df454f00-8b9c-4135-b8b2-7780ad3d83f0'

response = client.service.ConsultaEstatusSat(usuarioIntegrador = usuarioIntegrador, folioUUID = UUID)
tipoExepcion, codigoError, descripcion, Xml, QR, CadenaOriginal, codigoInterno, descripcionInterna, Detalle = response

root = ET.fromstring(Xml)
    
#namespaces
ns = {"pf":"http://www.profact.com.mx"}


res = root.find('pf:RespuestaSat',namespaces=ns)

for child in res:
    tag_elements = child.tag.split("}")     #Separamos el namespace del nombre del tag
    tag = tag_elements[1]
    print(f'{tag} : {child.text}')

'''EstadoComprobante = res.find('pf:EstadoComprobante', ns)
EstadoSat = res.find('pf:EstadoSat', ns)
print(f"Estado del comprobante: {EstadoComprobante.text}")
print(f"Estado SAT: {EstadoSat.text}")
'''
