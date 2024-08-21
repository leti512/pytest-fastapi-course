from fastapi.testclient import TestClient
from main import client
import time
import logging

client = TestClient(client)

def test_read_item_in_milisegundos(benchmark, fixture_auth_token):
    benchmark.extra_info['max_rounds'] = 3  # Mínimo de 10 rondas
    @benchmark
    def get_item():
        headers = {
            "Authorization": f"Bearer {fixture_auth_token}"
        }
        response = client.get("/main/items", headers=headers)
        assert response.status_code == 200
    
    stats = benchmark.stats
    print("\n *************All Stats Metadata:***********")
    for attr in dir(stats):
        if not attr.startswith("__"):
            print(f"{attr}: {getattr(stats, attr)}")
    print("\n *************END Stats Metadata************")
    print(f"Tiempo miiiiiiiiiiii**nimo: {stats.stats.__dict__}")
    #logging.warning(f"Tiempo mínimo: {stats['min'] * 1_000_000:.2f}")
        

def test_performance(fixture_auth_token):
    start_time = time.time()

    # Código a medir
    headers = {"Authorization": f"Bearer {fixture_auth_token}"}
    response = client.get("/main/items", headers=headers)
    assert response.status_code == 200

    end_time = time.time()
    execution_time = (end_time - start_time) * 1_000  # Convertir a microsegundos
    print(f"Execution time: {execution_time} milisegundos")



    
