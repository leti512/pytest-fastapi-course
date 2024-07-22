class Calculadora:
    
    
    def sumar(self, a: int, b:int) -> int:
        return a + b
    
    @classmethod
    def restar(cls, a: int, b:int) -> int:
        return a - b
    
    @classmethod
    def dividir(cls, a: int, b:int) -> float:
        return a / b
    
    
        