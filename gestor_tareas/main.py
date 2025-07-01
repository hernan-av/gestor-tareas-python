from rich import print
from tareas import crear_tarea, marcar_tarea_completada, eliminar_tarea
from persistencia import cargar_tareas, guardar_tareas, inicializar_archivo
from interfaz import mostrar_menu_principal, mostrar_tareas_en_tabla

# Inicia el programa: carga datos, muestra menú, y ejecuta acciones del usuario.
def main():
    inicializar_archivo()
    tareas = cargar_tareas()

    print("\n" + "─" * 60)
    print("[white on dark_blue bold]" + " GESTOR DE TAREAS ".center(60) + "[/]")
    print("─" * 60 + "\n")

    while True:
        print("\n[bold steel_blue3]" + "─" * 22 + " Menú principal " + "─" * 22 + "[/]\n")
        opcion = mostrar_menu_principal()

        if opcion == "1":
            print("\n[bold medium_purple]" + "─" * 24 + " Ver tareas " + "─" * 24 + "[/]\n")
            mostrar_tareas_en_tabla(tareas)

        elif opcion == "2":
            print("\n[aquamarine1]" + "─" * 20 + " Crear nueva tarea " + "─" * 21 + "[/]\n")
            nueva = crear_tarea(tareas)
            if nueva:
                tareas.append(nueva)
                guardar_tareas(tareas)

        elif opcion == "3":
            print("\n[cyan]" + "─" * 18 + " Marcar como completada " + "─" * 18 + "[/]\n")
            marcar_tarea_completada(tareas)
            guardar_tareas(tareas)

        elif opcion == "4":
            print("\n[medium_purple]" + "─" * 22 + " Eliminar tarea " + "─" * 22 + "[/]\n")
            eliminar_tarea(tareas)
            guardar_tareas(tareas)

        elif opcion == "5":
            print("\n[bold cyan]" + "─" * 20 + " Programa finalizado " + "─" * 19 + "[/]\n\n")
            break

        else:
            print("\n[red bold]❌ Opción inválida. Ingresá un número del 1 al 5.[/]\n")

if __name__ == "__main__":
    main()
