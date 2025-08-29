class ListaDeTarefas:
    def __init__(self):
        self._tarefas = []

    def adicionar(self, tarefa):
        self._tarefas.append(tarefa)

    def remover(self, indice):
        return self._tarefas.pop(indice)

   
    def __len__(self):
        return len(self._tarefas)

    
    def __iter__(self):
        return iter(self._tarefas)

    
    def __getitem__(self, index):
        return self._tarefas[index]



if __name__ == "__main__":
    tarefas = ListaDeTarefas()
    tarefas.adicionar("Estudar Python")
    tarefas.adicionar("Imprimir luminária 3D")
    tarefas.adicionar("Postar no @RW__3D")

    print("Quantidade de tarefas:", len(tarefas))  

    for t in tarefas:  
        print("-", t)

    print("Primeira tarefa:", tarefas[0])  
