import unittest

class TestPrueba(unittest.TestCase):
    # 1- ARRANGE | PRECONFIGURACIÓN 
    def setUp(self):
        print("""
              #1 - CONFIGURANDO EL ENTORNO DE LOS TESTS
              - Se creo la conexion con la base de datos - OK
              """)
    
    def test_crear_usuario(self):
        print("""
              #2 - EJECUCION DE LAS LINEAS DEL TEST
              """)
        print("### Creando el usuario Pepe ###")
        print("### Creando con exito ###")
        assert True # 3 -ASSERT | EVALUACIÓN
        print("### Creado con exito ###")
        
    # 4 - CLEANUP | LIMPIEZA
    def tearDown(self):
        print("""
            #4 - Se esta eliminando los registros de la base de datos  
              """)