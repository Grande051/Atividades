from abc import ABC, abstractmethod


class Forma(ABC):
    @abstractmethod
    def area(self):
        """Método abstrato que deve ser implementado nas subclasses"""
        pass



class Quadrado(Forma):
    def __init__(self, lado):
        if lado < 0:
            raise ValueError("O lado não pode ser negativo")
        self.lado = lado

    def area(self):
        return self.lado * self.lado



if __name__ == "__main__":
    q = Quadrado(2)
    print("Lado:", q.lado)
    print("Área do quadrado:", q.area())
