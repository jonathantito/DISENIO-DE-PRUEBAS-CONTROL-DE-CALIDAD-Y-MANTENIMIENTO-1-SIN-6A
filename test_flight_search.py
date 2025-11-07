import pytest
from datetime import datetime

def buscar_vuelos(origen, destino, fecha):
    if not origen or not destino:
        return "Error: campos vacíos"
    fecha_viaje = datetime.strptime(fecha, "%Y-%m-%d")
    if fecha_viaje < datetime.now():
        return "Error: fecha inválida"
    return "Búsqueda exitosa"

@pytest.mark.parametrize("origen,destino,fecha,esperado", [
    ("Quito", "Guayaquil", "2025-12-01", "Búsqueda exitosa"),     # partición válida
    ("", "Guayaquil", "2025-12-01", "Error: campos vacíos"),      # origen vacío
    ("Quito", "", "2025-12-01", "Error: campos vacíos"),          # destino vacío
    ("Quito", "Guayaquil", "2024-01-01", "Error: fecha inválida") # fecha pasada
])
def test_buscar_vuelos(origen, destino, fecha, esperado):
    assert buscar_vuelos(origen, destino, fecha) == esperado