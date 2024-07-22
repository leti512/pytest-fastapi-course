import pytest

@pytest.fixture()
def base_de_datos():
    print("\n ARRANGE | SETUP | PRECONFIGURACIÓN")
    yield
    print("\n CLEAN UP | TEAR DOWN | LIMPIEZA")

def test_prueba(base_de_datos):
    print("\n EJECUCION")
    assert True

def test_prueba2(base_de_datos):
    print("\n EJECUCION 2")
    assert False
    print("ESTO NO SE EJECUTA")
    