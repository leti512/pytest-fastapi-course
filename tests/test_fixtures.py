
class TestsFixtures:

    def test_prueba(self, fixture_nombre):
        assert fixture_nombre == "Facundo"
    

    def test_suma_de_impares(self, numero_impar):
        nro1 = numero_impar()
        nro2 = numero_impar()
        print(nro1, nro2)
        assert (nro1 + nro2) % 2 == 0


