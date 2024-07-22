import pytest
import sys
 
# def verificar_variables_de_entorno():
#     return False

# def test_prueba():
#     if not verificar_variables_de_entorno():
#         pytest.skip("Las variables de entorno no estań bien configuradas")

# @pytest.mark.skip(reason="Este test es de prueba")
# def test_prueba2():
#     assert False
    
#skip condicional
# @pytest.mark.skipif(True, reason="Test skipeado")
# def test_prueba3():
#     assert False

# @pytest.mark.skipif(verificar_variables_de_entorno() is False, reason="Test skipeado")
# def test_prueba4():
#     assert False

# @pytest.mark.skipif(sys.platform == "linux" , reason="Test skipeado porque no corre en linux")
# def test_prueba4():
#     assert False

##### xfail
# @pytest.mark.xfail
# def test_pruebaA():
#     print("SE ESTA EJECUTANDO NORMALMENTE, SI EL ASSERT ES FALSESE IGNORA/SKIPPEAY SINO, PASA NORMALMENTE")
#     assert False

# @pytest.mark.xfail
# def test_pruebaB():
#     assert True

### fixtures en clases 

    
@pytest.fixture
def prueba():
    print("\n soy una prueba y me ejecuto cada vez que me invocan")

@pytest.fixture
def prueba_2():
    print("\n fixture nro2")
    

@pytest.mark.usefixtures("prueba", "prueba_2")
class TestPrueba:

    def test_1(self):
        pass

    def test_2(self):
        pass
    
    def test_3(self):
        pass
    
    def test_4(self):
        pass
    
    def test_5(self):
        pass
    


    