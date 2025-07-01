from rich import print
from rich.table import Table
from rich.console import Console

console = Console()

# Muestra el menú principal y devuelve la opción elegida por el usuario.
def mostrar_menu_principal() -> str:
    print("\n[bold steel_blue3]Seleccione una opción:[/]\n")
    print("[white]1.[/] Ver tareas")
    print("[white]2.[/] Crear nueva tarea")
    print("[white]3.[/] Marcar tarea como completada")
    print("[white]4.[/] Eliminar tarea")
    print("[white]5.[/] Salir\n")

    return console.input("[bold steel_blue3]Ingresá una opción (1-5): [/]").strip()

# Muestra todas las tareas en una tabla con colores según prioridad y estado.
def mostrar_tareas_en_tabla(tareas: list) -> None:
    if not tareas:
        print("\n[yellow]📭 No hay tareas para mostrar.[/]\n")
        return

    tabla = Table(title=None, show_lines=True)

    tabla.add_column("ID", style="bold cyan", justify="right")
    tabla.add_column("Título", style="bold white")
    tabla.add_column("Descripción", style="dim white")
    tabla.add_column("Prioridad", style="bold")
    tabla.add_column("Estado", style="bold")

    for t in tareas:
        prioridad_color = {
            "Alta": "[bold red]Alta[/]",
            "Media": "[bold yellow]Media[/]",
            "Baja": "[bold green]Baja[/]"
        }[t["prioridad"]]

        estado_color = {
            "Pendiente": "[cyan]Pendiente[/]",
            "Completada": "[medium_orchid]Completada[/]"
        }[t["estado"]]

        tabla.add_row(
            str(t["id"]),
            t["titulo"],
            t["descripcion"],
            prioridad_color,
            estado_color
        )

    console.print(tabla)

# Muestra una tarea individual con sus detalles.
def mostrar_tarea(tarea: dict, encabezado: str = "") -> None:
    if encabezado:
        print(f"\n[grey62]{encabezado}[/]\n")

    print(f"[grey62] Id:          [/][white]{tarea['id']}")
    print(f"[grey62] Título:      [/][white]{tarea['titulo']}")
    print(f"[grey62] Descripción: [/][white]{tarea['descripcion']}")
    print(f"[grey62] Prioridad:   [/][white]{tarea['prioridad']}")
    print(f"[grey62] Estado:      [/][white]{tarea['estado']}")