from fastapi.testclient import TestClient
from src.pytest_examples.app import client

client = TestClient(client)