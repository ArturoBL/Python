import yaml

config = {
    "database": {
        "driver": "sqlite",
        "database": "app.db",
        "host": "0.0.0.0"
    },
    "app": {
        "debug": True
    }
}

with open("config.yaml", "w", encoding="utf-8") as file:
    yaml.dump(
        config,
        file,
        default_flow_style=False,
        allow_unicode=True
    )