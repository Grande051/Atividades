"""
Exercício 1
-------------
Crie uma classe Livro com @property para estoque que proíba números negativos.
"""
from dataclasses import dataclass, field

@dataclass
class Livro:
    titulo: str
    autor: str
    _estoque: int = field(default=0, repr=False)

    def __post_init__(self):
        self.estoque = self._estoque  # valida no setter

    @property
    def estoque(self) -> int:
        """Quantidade disponível em estoque."""
        return self._estoque

    @estoque.setter
    def estoque(self, valor: int) -> None:
        if not isinstance(valor, int):
            raise TypeError("estoque deve ser um inteiro")
        if valor < 0:
            raise ValueError("estoque não pode ser negativo")
        self._estoque = valor

    def adicionar(self, quantidade: int) -> None:
        if quantidade < 0:
            raise ValueError("quantidade para adicionar não pode ser negativa")
        self.estoque = self.estoque + quantidade

    def remover(self, quantidade: int) -> None:
        if quantidade < 0:
            raise ValueError("quantidade para remover não pode ser negativa")
        novo = self.estoque - quantidade
        if novo < 0:
            raise ValueError("remoção resultaria em estoque negativo")
        self.estoque = novo

if __name__ == "__main__":
    livro = Livro("Estruturas de Dados em Python", "Alguém", 10)
    print("Estoque inicial:", livro.estoque)
    livro.adicionar(5)
    print("Após adicionar 5:", livro.estoque)
    try:
        livro.remover(20)
    except ValueError as e:
        print("Erro esperado:", e)
    livro.remover(3)
    print("Após remover 3:", livro.estoque)
