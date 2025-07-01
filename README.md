# Gestor de Tareas en Python

Aplicación de consola desarrollada en Python. Permite al usuario crear, visualizar, completar y eliminar tareas, con una interfaz enriquecida mediante la biblioteca `rich`. El objetivo es demostrar buenas prácticas de modularización, validación y experiencia de usuario en un entorno de consola.

---

## Funcionalidad principal

- Ver tareas en formato de tabla con colores e íconos.
- Crear nuevas tareas (con título, descripción y prioridad).
- Marcar tareas como completadas.
- Eliminar tareas por ID.
- Guardado automático en `data/tareas.json`.
- Cancelación de cualquier acción ingresando `'c'`.

---

## Cómo ejecutar el programa

1. Cloná este repositorio o descargalo como ZIP.
2. Instalá dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecutá el sistema desde consola:

```bash
# En Windows
python gestor_tareas/main.py

# En Linux/macOS
python3 gestor_tareas/main.py
```

El sistema iniciará con un menú interactivo.

---

## Estructura del proyecto

```
data/                     # Archivo de tareas en JSON
└── tareas.json

gestor_tareas/            # Código fuente del sistema
├── entrada_datos.py      # Solicita y valida entradas del usuario
├── interfaz.py           # Menús y visualizaciones con Rich
├── logs.py               # Registro de eventos importantes
├── main.py               # Bucle principal del programa
├── persistencia.py       # Manejo de lectura y guardado en JSON
└── tareas.py             # Lógica para crear, completar y eliminar tareas

README.md                 # Documentación del proyecto
requirements.txt          # Dependencias del proyecto
registro.log              # Log generado automáticamente
```

---

## Ejemplo de una tarea

```bash
{
    "id": 6,
    "titulo": "Compras Supermercado",
    "descripcion": "Compras del Mes",
    "prioridad": "Alta",
    "estado": "Pendiente"
}
```

Todas las acciones tienen validaciones. Se puede cancelar cualquier entrada ingresando `'c'`.

---

## Datos precargados

El archivo `data/tareas.json` incluye tareas de ejemplo para facilitar la evaluación del flujo completo. El sistema es funcional desde el primer uso.

---

## Consideraciones de diseño

* Separación lógica por módulos (única responsabilidad por archivo).
* Validación completa en todas las entradas del usuario.
* Interfaz enriquecida con rich: colores, íconos, tablas y feedback.
* Registro de eventos importantes en `registro.log`.

---

## Posibles mejoras futuras

- Filtros por prioridad o estado.
- Agrupamiento por categorías o etiquetas.
- Exportación de tareas completadas a otro archivo.

---

## Requisitos

* Python 3.10+
* Biblioteca [`rich`](https://pypi.org/project/rich/)

Instalación rápida:

```bash
pip install -r requirements.txt
```

---

## Nota final

Este proyecto fue desarrollado como parte del segundo parcial con foco en legibilidad, validación robusta, modularización y claridad para el usuario final.

---
