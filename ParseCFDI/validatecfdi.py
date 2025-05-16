from lxml import etree

def validar_cfdi(xml_path: str, xsd_path: str) -> bool:
    try:
        # Cargar el esquema XSD
        with open(xsd_path, 'rb') as f:
            xsd_doc = etree.parse(f)
            schema = etree.XMLSchema(xsd_doc)

        # Cargar el XML CFDI
        with open(xml_path, 'rb') as f:
            xml_doc = etree.parse(f)

        # Validar
        schema.assertValid(xml_doc)
        print("✅ CFDI válido según el XSD.")
        return True

    except etree.DocumentInvalid as e:
        print("❌ CFDI inválido:", e)
        return False
    except Exception as e:
        print("⚠️ Error durante la validación:", e)
        return False


res = validar_cfdi(r'C:\temp\B003055.xml', r'c:\temp\cfdv40.xsd')
print(res)
