# Diferencias de rendimiento


| Método                   | Rendimiento | Facilidad | Recomendado              |
| ------------------------ | ----------- | --------- | ------------------------ |
| ORM clásico (`query`)    | Medio       | Alto      | Sólo legado              |
| ORM moderno (`select`)   | Bueno       | Alto      | ✔ Sí                     |
| ORM columnas específicas | Muy bueno   | Alto      | ✔✔                       |
| `session.get()`          | Excelente   | Alto      | ✔✔                       |
| ORM + `joinedload`       | Muy bueno   | Medio     | ✔✔                       |
| SQLAlchemy Core          | Excelente   | Medio     | ✔✔ para alto rendimiento |
| SQL RAW                  | Máximo      | Bajo      | Casos especiales         |