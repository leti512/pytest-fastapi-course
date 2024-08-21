from fastapi.testclient import TestClient
from main import client
import time
import logging

client = TestClient(client)

def test_read_item_in_microseconds(benchmark, fixture_auth_token):
    @benchmark
    def get_item():
        headers = {
            "Authorization": f"Bearer {fixture_auth_token}"
        }
        response = client.get("/main/items", headers=headers)
        assert response.status_code == 200
        #Supongamos que la respuesta es un JSON y contiene una lista de resultados
        data = response.json()
        result_count = len(data['items'])  # Suponiendo que los resultados están bajo la clave 'results'

        # Simulación o verificación del número de resultados
        assert result_count > 0  # Asegura que haya al menos un resultado

        # Obtener el objeto Metadata
    metadata = benchmark

    # Obtener el objeto Stats desde Metadata
    stats = metadata.stats
    
    print("\nAll Stats Metadata:")
    for attr in dir(stats):
        if not attr.startswith("__"):
            print(f"{attr}: {getattr(stats, attr)}")
    print(f"Mean time: {stats.mean:.6f} seconds")
    # mean_time_microseconds = stats.mean * 1_000_000
    # median_time_microseconds = stats.median * 1_000_000

    # # Logging de los resultados
    # logging.warning(f"Mean time: {mean_time_microseconds} microseconds")
    # logging.warning(f"Median time: {median_time_microseconds} microseconds")
    # #logging.warning(f"Number of results: {result_count}")

    # # Asserts para asegurarse de que el tiempo está dentro de un rango aceptable
    # assert mean_time_microseconds < 500_000  # 500 ms
    # assert median_time_microseconds < 500_000  # 500 ms
