from datetime import datetime

class RegistroContexto:
    def __init__(self, arquivo):
        self.arquivo = arquivo

    def __enter__(self):
        with open(self.arquivo, "a", encoding="utf-8") as f:
            f.write(f"Começo - {datetime.now().isoformat()}\n")
        return self

    def __exit__(self, tipo, valor, traceback):
        with open(self.arquivo, "a", encoding="utf-8") as f:
            f.write(f"Fim    - {datetime.now().isoformat()}\n")
        
        return False



if __name__ == "__main__":
    with RegistroContexto("log.txt"):
        print("Executando algo dentro do contexto...")
