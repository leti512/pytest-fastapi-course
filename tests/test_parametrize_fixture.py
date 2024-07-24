# import pytest

# @pytest.fixture()
# def fixture_prueba(request):
#     return request.param

# @pytest.mark.parametrize(
#     "fixture_prueba",
#     [
#         555,
#         "esto es un string",
#         (1,2,3,4),
#         {"calve": "valor"}
#     ],
#     indirect=True
#     #o indirect=["fixture_prueba"]
# )
# def test_prueba(fixture_prueba):
#     assert True

import pytest

class Usuario:
    
    def __init__(self, nombre: str, rol:str):
        self.nombre = nombre
        self.rol = rol
    
def ingresar_a_la_boveda(usuario: Usuario):
    if usuario.rol in ["administrador", "cliente"]:
        return True
    return False

@pytest.fixture
def usuario(request):
    return Usuario(nombre=request.param["nombre"], rol=request.param["rol"])

# @pytest.mark.parametrize(
#     "usuario",
#     [
#         {"nombre": "Facundo", "rol": "administrador"},
#         {"nombre": "Pepe", "rol": "cliente"},
#         {"nombre": "Pancho", "rol": "invitado"}
#     ],
#     indirect=True
#    )
# def test_roles(usuario):
#     if usuario.rol in ["administrador", "cliente"]:
#         assert ingresar_a_la_boveda(usuario)
#     else:
#         assert ingresar_a_la_boveda(usuario) is False
#     print(usuario)   
    
# @pytest.mark.parametrize(
#     "usuario",
#     [
#         {"nombre": "Facundo", "rol": "administrador", "expected_response": True},
#         {"nombre": "Pepe", "rol": "cliente", "expected_response":  True},
#         {"nombre": "Pancho", "rol": "invitado", "expected_response": False}
#     ],
#     indirect=True
#    )
# def test_roles(request, usuario):
#     assert ingresar_a_la_boveda(usuario) == request.node.callspec.params["usuario"]["expected_response"]
#     print(usuario)    

import pytest
import pprint

@pytest.fixture
def usuario(request):
    # `request.param` es el parámetro pasado a través de `pytest.mark.parametrize`
    return request.param

@pytest.mark.parametrize(
    "usuario",
    [
        {"nombre": "Facundo", "rol": "administrador", "expected_response": True},
        {"nombre": "Pepe", "rol": "cliente", "expected_response": True},
        {"nombre": "Pancho", "rol": "invitado", "expected_response": False}
    ],
    indirect=True
)
def test_roles(request, usuario):
    # Imprime la estructura del objeto request para explorar sus atributos
    pprint.pprint(vars(request))
    pprint.pprint(vars(request.node))
    pprint.pprint(vars(request.node.callspec))

    # Simulación de una función que verifica el rol de usuario para ingresar a la bóveda
    def ingresar_a_la_boveda(usuario):
        if usuario["rol"] in ["administrador", "cliente"]:
            return True
        else:
            return False

    # Asegúrate de que la respuesta esperada coincida con la respuesta de la función
    assert ingresar_a_la_boveda(usuario) == request.node.callspec.params["usuario"]["expected_response"]
    print(usuario)

if __name__ == "__main__":
    pytest.main()

    
