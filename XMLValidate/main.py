from lxml import etree
'''
    Para validar hay que tener los siguientes datos en el archivo pretimbrado:
                Sello="HfK..."
                  Certificado="MIIGJTCC..."
				  NoCertificado="00..."
'''                  
def validar_cfdi(xml_path, xsd_path):
    try:
        # Cargar el esquema XSD
        with open(xsd_path, 'rb') as xsd_file:
            schema_doc = etree.parse(xsd_file)
            schema = etree.XMLSchema(schema_doc)

        # Cargar el CFDI (XML)
        with open(xml_path, 'rb') as xml_file:
            xml_doc = etree.parse(xml_file)

        # Validar
        schema.assertValid(xml_doc)
        print("✅ El CFDI es válido conforme al esquema XSD.")
        return True

    except etree.DocumentInvalid as e:
        print("❌ El CFDI no es válido:")
        print(e)
        return False
    except Exception as ex:
        print("⚠️ Error al procesar los archivos:")
        print(ex)
        return False

# Ejemplo de uso
xml_cfdi = 'B003096.xml'
xsd_cfdi = 'cfdv40.xsd'  # o el nombre del archivo de esquema que estés usando

validar_cfdi(xml_cfdi, xsd_cfdi)
