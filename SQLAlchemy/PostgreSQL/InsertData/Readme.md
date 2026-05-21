# Métodos de inserción


| Método              | Rendimiento | Ventajas                       | Desventajas             |
| ------------------- | ----------- | ------------------------------ | ----------------------- |
| `exec_driver_sql()` | Máximo      | Muy bajo overhead              | Poco portable           |
| `text()`            | Muy alto    | Flexible y portable            | Menos integración ORM   |
| `insert()` Core     | Alto        | Portable y elegante            | Algo más overhead       |
| `session.add()` ORM | Medio/Bajo  | Objetos completos y relaciones | Más consumo CPU/memoria |

