import pytest
# def test_1(fixture_5):
#     print(fixture_5)

# def test_6(fixture_5):
#     print(fixture_5)

# @pytest.fixture
# def leer_archivo():
#     with open("archivo.txt", "r") as file:
#         texto = file.read()
    
#     return texto

# def test_especifico(leer_archivo):
#    pass
@pytest.fixture
def operacion_ligera():
    lista = [1,2,3]
    return sum(lista)

def test_operacion_ligera():
    pass
