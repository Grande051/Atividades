
class Relogio:
    def __init__(self, hora: int, minuto: int):
        if not (0 <= hora <= 23):
            raise ValueError("hora deve estar entre 0 e 23")
        if not (0 <= minuto <= 59):
            raise ValueError("minuto deve estar entre 0 e 59")
        self.hora = hora
        self.minuto = minuto

    def __str__(self) -> str:
        return f"{self.hora:02d}:{self.minuto:02d}"

    def __repr__(self) -> str:
        return f"Relogio(hora={self.hora}, minuto={self.minuto})"

if __name__ == "__main__":
    r = Relogio(17, 35)
    print(str(r))   
    print(repr(r))  