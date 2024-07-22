from unittest.mock import patch

class Perro:
    def ladrar(self):
        return "woof"

perro = Perro()
print(perro.ladrar())
with patch.object(target=Perro, attribute="ladrar") as mock_perro:
    mock_perro.return_value = "esto es un mock y es una prueba"
    print(perro.ladrar())
"""

"""
