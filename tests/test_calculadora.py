import pytest 
from src.pytest_examples.services.calculadora import Calculadora

class TestCalculadora:
    @pytest.mark.parametrize (
        "nro1,nro2,expected", [
            (1,5,6),
            (10,10,20),
            (50,1,51)
            ]
    )
    def test_sumar(self, nro1, nro2, expected):
        calculadora = Calculadora()
        resultado = calculadora.sumar(nro1,nro2)
        assert resultado == expected

    def test_restar(self):
        resultado = Calculadora.restar(5,5)
        assert resultado == 0
        
    def test_dividir(self):
        resultado = Calculadora.dividir(6, 3)
        assert resultado == 2