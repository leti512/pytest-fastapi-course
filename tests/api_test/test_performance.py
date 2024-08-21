from fastapi.testclient import TestClient
from main import client
import time

client = TestClient(client)

def test_read_item(benchmark):
    @benchmark
    def get_item():
        response = client.get("/main/items")
        assert response.status_code == 200
        
        
        
        
# def test_read_itemv2():
#     #starting time
#     start = time.time()
#     def get_item_time():
#         response = client.get("/main/items")
#         assert response.status_code == 200
#     # end time
#     end = time.time()
#     # total time taken
#     print("Execution time of the program is- ", end-start)
    
# def test_read_itemv2():
#     # Starting time
#     start = time.perf_counter()
    
#     response = client.get("/items")
#     #assert response.status_code == 200
    
#     # End time
#     end = time.time()
    
#     execution_time_microseconds = (end - start) * 1_000_000  
#     execution_time = end - start
#     print("Execution time of the program is- ", execution_time_microseconds, " microseconds")
#     print("Execution is- ", execution_time, " seconds")
