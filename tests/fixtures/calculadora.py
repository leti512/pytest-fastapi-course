import random
import pytest

#no se pueden usar dos fixtures en la misma función
@pytest.fixture()
def numero_impar():
    def generar_numero():
        while True:
            numero = random.randint(1, 100)
            if numero %2 != 0:
                return numero
    yield generar_numero