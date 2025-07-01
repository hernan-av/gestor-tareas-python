from entrada_datos import pedir_titulo, pedir_descripcion, pedir_prioridad, CANCELADO
from interfaz import mostrar_tareas_en_tabla, mostrar_tarea
from logs import registrar_evento
from rich.console import Console
from rich import print

console = Console()

# Verifica si ya existe una tarea con el mismo título.
# Si encuentra duplicado, solicita confirmación al usuario.
def verificar_tarea_duplicada(tareas: list, titulo: str) -> bool:
    titulo = titulo.strip().lower()

    for tarea in tareas:
        titulo_existente = tarea["titulo"].strip().lower()

        if titulo == titulo_existente:
            print("\n[yellow]⚠️ Ya existe una tarea con el mismo título:[/]\n")
            mostrar_tarea(tarea)

            while True:
                respuesta = console.input("\n[medium_purple italic]¿Deseás agregar igualmente esta nueva tarea? (s / n): [/]").strip().lower()

                if respuesta == "s":
                    return True
                elif respuesta == "n":
                    return False

                print("\n[yellow]⚠️ Respuesta inválida. Solo se acepta 's' o 'n'.[/]")

    return True

# Crea una nueva tarea con validación de entradas y duplicados.
# Devuelve el diccionario de la tarea o None si se cancela.
def crear_tarea(tareas: list) -> dict | None:
    ids_existentes = []
    for tarea in tareas:
        ids_existentes.append(tarea["id"])

    nuevo_id = max(ids_existentes, default=0) + 1

    titulo = pedir_titulo(25)
    if titulo == CANCELADO:
        print("\n[yellow]↩️ Acción cancelada. Volviendo al menú principal.[/]\n")
        return None

    descripcion = pedir_descripcion(60)
    if descripcion == CANCELADO:
        print("\n[yellow]↩️ Acción cancelada. Volviendo al menú principal.[/]\n")
        return None

    prioridad = pedir_prioridad()
    if prioridad == CANCELADO:
        print("\n[yellow]↩️ Acción cancelada. Volviendo al menú principal.[/]\n")
        return None

    if not verificar_tarea_duplicada(tareas, titulo):
        print("\n[yellow]↩️ Acción cancelada. Volviendo al menú principal.[/]\n")
        return None

    nueva_tarea = {
        "id": nuevo_id,
        "titulo": titulo,
        "descripcion": descripcion,
        "prioridad": prioridad,
        "estado": "Pendiente"
    }

    print("\n[green bold]✅ Tarea guardada correctamente.[/]\n")
    mostrar_tarea(nueva_tarea, "Tarea creada:")
    registrar_evento(f"Tarea creada: ID {nueva_tarea['id']} - {nueva_tarea['titulo']}")

    return nueva_tarea

# Marca como completada una tarea pendiente seleccionada por ID.
# Muestra advertencia si el ID no es válido
def marcar_tarea_completada(tareas: list) -> None:
    tareas_pendientes = []
    for t in tareas:
        if t["estado"].lower() == "pendiente":
            tareas_pendientes.append(t)

    if not tareas_pendientes:
        print("\n[yellow]⚠️ No hay tareas pendientes para completar.[/]\n")
        return

    print("\n[cyan]Tareas pendientes actuales:[/]\n")
    mostrar_tareas_en_tabla(tareas_pendientes)

    while True:
        seleccion = console.input("[cyan]\nIngresá el ID a marcar como completada (número entero | 'c' para cancelar): [/]").strip()

        if seleccion.lower() == CANCELADO:
            print("\n[yellow]↩️ Acción cancelada. Volviendo al menú principal.[/]\n")
            return

        try:
            id_ingresado = int(seleccion)
            tarea_seleccionada = None
            for t in tareas_pendientes:
                if t["id"] == id_ingresado:
                    tarea_seleccionada = t
                    break

            if tarea_seleccionada:
                tarea_seleccionada["estado"] = "Completada"
                print("\n[green bold]✅ Tarea marcada como completada.[/]\n")
                mostrar_tarea(tarea_seleccionada, "Estado actualizado:")
                registrar_evento(f"Tarea completada: ID {tarea_seleccionada['id']} - {tarea_seleccionada['titulo']}")
                return

            print("\n[red bold]❌ No se encontró una tarea pendiente con ese ID.[/]")

        except ValueError:
            print("\n[red bold]❌ El ID ingresado no es válido. Ingresá un número entero.[/]")

# Elimina una tarea seleccionada por ID. Verifica existencia antes de eliminar.
def eliminar_tarea(tareas: list) -> None:
    if not tareas:
        print("\n[yellow]⚠️ No hay tareas disponibles para eliminar.[/]\n")
        return

    print("\n[medium_purple]Lista de tareas disponibles para eliminar:[/]\n")
    mostrar_tareas_en_tabla(tareas)

    while True:
        seleccion = console.input("[medium_purple]\nIngresá el ID de la tarea a eliminar (número entero | 'c' para cancelar): [/]").strip()

        if seleccion.lower() == CANCELADO:
            print("\n[yellow]↩️ Acción cancelada. Volviendo al menú principal.[/]\n")
            return

        try:
            id_ingresado = int(seleccion)
            tarea_a_eliminar = None
            for tarea in tareas:
                if tarea["id"] == id_ingresado:
                    tarea_a_eliminar = tarea
                    break

            if tarea_a_eliminar:
                tareas.remove(tarea_a_eliminar)
                print("\n[green bold]✅ Tarea eliminada correctamente.[/]\n")
                mostrar_tarea(tarea_a_eliminar, "Tarea eliminada:")
                registrar_evento(f"Tarea eliminada: ID {tarea_a_eliminar['id']} - {tarea_a_eliminar['titulo']}")
                return

            print("\n[red bold]❌ No se encontró ninguna tarea con ese ID.[/]")

        except ValueError:
            print("\n[red bold]❌ El ID ingresado no es válido. Debe ser un número entero.[/]")
