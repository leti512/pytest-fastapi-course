import pytest
import random

@pytest.fixture(scope="class")
def nro_random(request):
    return random.randint(1, 100)

class TestPrueba:
    
    def test_1(self, nro_random):
        print("\n", nro_random)
    
    def test_2(self, nro_random):
        print("\n", nro_random)