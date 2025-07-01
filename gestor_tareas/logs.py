import logging
from pathlib import Path

# Ruta al archivo de log (ubicado en la raíz del proyecto)
RUTA_LOG = Path(__file__).parent.parent / "registro.log"

# Configuración básica del logger
logging.basicConfig(
    filename=RUTA_LOG,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Registra un evento en el archivo de log con nivel (como crear, completar o eliminar tareas)
# Soporta niveles `info`, `warning` y `error`.
def registrar_evento(mensaje: str, nivel: str = "info") -> None:
    nivel = nivel.lower()
    if nivel == "info":
        logging.info(mensaje)
    elif nivel == "warning":
        logging.warning(mensaje)
    elif nivel == "error":
        logging.error(mensaje)