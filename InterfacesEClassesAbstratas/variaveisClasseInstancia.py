class Estudante:
    escola = "DIO" # Variaveis de classe são definidas dentro da classe

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"
    

aluno1 = Estudante("Lucas", 123124) # Intancias são do objeto
aluno2 = Estudante("Eduardo", 123124)
print(aluno1)
print(aluno2)

Estudante.escola = "Python"