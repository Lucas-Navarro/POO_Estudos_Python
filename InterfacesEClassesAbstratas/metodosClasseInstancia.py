class Pessoa:
    def __init__(self, nome= None, idade = None):
        self.nome = nome
        self.idade = idade

    @classmethod # Utilizado para complementar metodos de instacnias, sendo bom para ajudar a crirar novos métodos
    def criar_data_nasc(cls, ano, mes, dia, nome):
        idade = 2026 - ano
        return cls(nome, idade) # Preciso do contexto da classe? Então método de classe
    
    @staticmethod # Não preciso de contexto e nem de classe 
    def e_maior_idade(idade):
        return idade >= 18


p = Pessoa.criar_data_nasc(2004, 10, 27, "Lucas")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(10))