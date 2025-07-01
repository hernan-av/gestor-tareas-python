from rich import print
from rich.console import Console

console = Console()
CANCELADO = "c" #Constante utilizada para detectar y manejar salidas voluntarias

# Solicita un título válido al usuario (no vacío, con capitalización).
# Permite cancelar con 'c'.
def pedir_titulo(max_largo: int) -> str:
    while True:
        titulo = console.input(f"\n[aquamarine1]- Ingresá el título (máx {max_largo} caracteres | 'c' para cancelar): [/]").strip()

        if titulo.lower() == "c":
            return CANCELADO

        if titulo and len(titulo) <= max_largo:
            return titulo[0].upper() + titulo[1:]

        print(f"\n[yellow]⚠️ El título no puede estar vacío ni superar {max_largo} caracteres. Ingresaste {len(titulo)} caracteres.[/]")

# Solicita una descripción válida (no vacía y dentro del largo permitido).
# Permite cancelar con 'c'. 
def pedir_descripcion(max_largo: int) -> str:
    while True:
        descripcion = console.input(f"\n[aquamarine1]- Ingresá la descripción (máx {max_largo} caracteres | 'c' para cancelar): [/]").strip()

        if descripcion.lower() == "c":
            return CANCELADO
        
        if descripcion and len(descripcion) <= max_largo:
            return descripcion[0].upper() + descripcion[1:]

        print(f"\n[yellow]⚠️ La descripción no puede estar vacía ni superar {max_largo} caracteres. Ingresaste {len(descripcion)} caracteres.[/]")

# Solicita una prioridad válida ('alta', 'media', 'baja').
# Permite cancelar con 'c'.
def pedir_prioridad() -> str:
    opciones_validas = ["alta", "media", "baja"]

    while True:
        prioridad = console.input("\n[aquamarine1]- Ingresá la prioridad (alta / media / baja | 'c' para cancelar): [/]").strip().lower()

        if prioridad.lower() == "c":
            return CANCELADO

        if prioridad in opciones_validas:
            return prioridad.capitalize()

        print("\n[yellow]⚠️ Prioridad inválida. Por favor, ingresá: alta, media o baja.[/]")