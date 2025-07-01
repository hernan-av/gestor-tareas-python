import json
from pathlib import Path
from rich import print

RUTA_JSON = Path(__file__).parent.parent / "data" / "tareas.json"

# Crea el archivo tareas.json vacío si no existe. Informa errores de escritura.
def inicializar_archivo():
    try:
        if not RUTA_JSON.exists():
            with open(RUTA_JSON, "w", encoding="utf-8") as archivo:
                json.dump([], archivo, indent=4)
                print("\n[green bold]✅ Archivo tareas.json creado con una lista vacía.[/]\n")
    except Exception as e:
        print(f"\n[red bold]❌ Ocurrió un error al crear/inicializar el archivo .json: {e}[/]\n")
    return True

# Carga las tareas desde el archivo JSON. Si no se puede leer, retorna lista vacía.
def cargar_tareas():
    try:
        with open(RUTA_JSON, "r", encoding="utf-8") as archivo:
            tareas = json.load(archivo)
            return tareas
    except FileNotFoundError:
        print("\n[yellow]⚠️ El archivo de tareas no fue encontrado. Se usará una lista vacía.[/]\n")
    except json.JSONDecodeError:
        print("\n[yellow]⚠️ El archivo existe, pero su contenido no es válido. Se iniciará una lista vacía.[/]\n")
    except Exception as e:
        print(f"\n[red bold]❌ Ocurrió un error inesperado al leer las tareas: {e}[/]\n")
    return []

# Guarda la lista de tareas en el archivo JSON con indentación.
def guardar_tareas(tareas):
    try:
        with open(RUTA_JSON, "w", encoding="utf-8") as archivo:
            json.dump(tareas, archivo, indent=4)
    except Exception as e:
        print(f"\n[red bold]❌ Ocurrió un error al guardar las tareas: {e}[/]\n")
