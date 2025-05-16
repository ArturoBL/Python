import xml.etree.ElementTree as ET

# Cargar el archivo CFDI
tree = ET.parse(r'M:\Timbrado\Timbradas\B003054.xml')
root = tree.getroot()

namespaces = {
    'cfdi': 'http://www.sat.gob.mx/cfd/4',         # para CFDI 4.0
    'tfd': 'http://www.sat.gob.mx/TimbreFiscalDigital'
}

comprobante = root

# Emisor
emisor = comprobante.find('cfdi:Emisor', namespaces)
print('RFC Emisor:', emisor.attrib['Rfc'])
print('Nombre Emisor:', emisor.attrib.get('Nombre', ''))

# Receptor
receptor = comprobante.find('cfdi:Receptor', namespaces)
print('RFC Receptor:', receptor.attrib['Rfc'])
print('Nombre Receptor:', receptor.attrib.get('Nombre', ''))

# Totales
print('Subtotal:', comprobante.attrib['SubTotal'])
print('Total:', comprobante.attrib['Total'])
print('Moneda:', comprobante.attrib['Moneda'])

# Timbre Fiscal
timbre = root.find('.//tfd:TimbreFiscalDigital', namespaces)
if timbre is not None:
    print('UUID:', timbre.attrib['UUID'])
    print('Fecha Timbrado:', timbre.attrib['FechaTimbrado'])
    print('Sello CFDI:', timbre.attrib['SelloCFD'])
    print('Sello SAT:', timbre.attrib['SelloSAT'])


# Iterar por cada concepto
for concepto in root.findall('.//cfdi:Concepto', namespaces):
    print('\nDescripción:', concepto.attrib.get('Descripcion'))
    print('Importe:', concepto.attrib.get('Importe'))

    impuestos = concepto.find('cfdi:Impuestos', namespaces)
    if impuestos is not None:
        # Traslados por concepto
        traslados = impuestos.find('cfdi:Traslados', namespaces)
        if traslados is not None:
            for traslado in traslados.findall('cfdi:Traslado', namespaces):
                print('  [Traslado] Impuesto:', traslado.attrib['Impuesto'])
                print('             TipoFactor:', traslado.attrib['TipoFactor'])
                print('             TasaOCuota:', traslado.attrib.get('TasaOCuota', ''))
                print('             Importe:', traslado.attrib.get('Importe', ''))

        # Retenciones por concepto
        retenciones = impuestos.find('cfdi:Retenciones', namespaces)
        if retenciones is not None:
            for retencion in retenciones.findall('cfdi:Retencion', namespaces):
                print('  [Retención] Impuesto:', retencion.attrib['Impuesto'])
                print('               Importe:', retencion.attrib.get('Importe', ''))    


#obtener impuestos globales
impuestos_globales = root.find('cfdi:Impuestos', namespaces)
if impuestos_globales is not None:
    print('\n=== Impuestos Globales ===')
    total_ret = impuestos_globales.attrib.get('TotalImpuestosRetenidos')
    total_tras = impuestos_globales.attrib.get('TotalImpuestosTrasladados')

    if total_ret:
        print('Total Retenciones:', total_ret)
    if total_tras:
        print('Total Traslados:', total_tras)

    # Puedes también iterar por los impuestos globales detallados
    traslados_globales = impuestos_globales.find('cfdi:Traslados', namespaces)
    if traslados_globales is not None:
        for traslado in traslados_globales.findall('cfdi:Traslado', namespaces):
            print('  [Global Traslado] Impuesto:', traslado.attrib['Impuesto'])
            print('                     Importe:', traslado.attrib['Importe'])                