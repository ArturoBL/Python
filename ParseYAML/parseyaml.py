import yaml

# Leer el archivo YAML
with open("config.yaml", "r", encoding="utf-8") as archivo:
    config = yaml.safe_load(archivo)

# Acceder a datos
print("Nombre de la aplicación:", config["app"]["name"])
print("Versión:", config["app"]["version"])

for servidor in config["servidores"]:
    print(f"\nServidor: {servidor['nombre']} ({servidor['ip']})")
    for servicio in servidor["servicios"]:
        print(f"  - Servicio: {servicio['nombre']} (Puerto {servicio['puerto']})")

if config["notificaciones"]["activar"]:
    print("\nNotificaciones activadas. Contacto:", config["notificaciones"]["email"])
else:
    print("\nNotificaciones desactivadas.")
