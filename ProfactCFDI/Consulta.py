
from zeep import Client
import xml.dom.minidom
import sys
from SecretKey import UsuarioIntegrador

wsdl_url = 'https://timbracfdi33.mx:1443/Timbrado.asmx?WSDL'
client = Client(wsdl_url)

#obtenemos el UUID como parámetro de línea de comandos o se toma uno por defecto
n = len(sys.argv)
if n > 1:    
    UUID = sys.argv[1]         
else:
    #print('Debe indicar el UUID...')
    UUID = '5449e4aa-0122-414b-90ef-a7b82f23f649'
    print(f"Se procesa UUID por defecto: {UUID}")        

#Hacemos la petición
response = client.service.ConsultaEstatusSat(UsuarioIntegrador, UUID)
tipoexcepcion, codigo, descripcion, xmlstr, fill1, fill2, codigointerno, descripcioninterna, detalle = response

#procesamos el contenido de la respuesta XML
xml_doc = xml.dom.minidom.parseString(xmlstr)
root = xml_doc.documentElement
for child in root.childNodes:    
    if child.nodeName == 'RespuestaSat':   
        for cn in child.childNodes:     
            if len(cn.childNodes)>0:
                data = cn.childNodes[0].data
            print(f"{cn.nodeName}: {data}")



'''Parámetros petición
usuarioIntegrador: Token
folioUUID: Folio fiscal del CFDI que deseamos consultar

Parámetros de respuesta (arreglo de 9 posiciones)

Pos1: Tipo de excepción (En caso de error)
Pos2: Código (El código 0 representa una solicitud exitosa, cualquier otro código representa un error)
Pos3: Descripción (Descripción del error si aplica)
Pos4: Xml/acuse de consulta estatus SAT (Ver ejemplo)
Pos5: N/A
Pos6: N/A
Pos7: Código interno (Código de error interno para efectos de soporte)
Pos8: Descripción interna (Descripción interna del error para efectos de soporte)
Pos9: Detalle (Detalle de error en formato JSON)'''
