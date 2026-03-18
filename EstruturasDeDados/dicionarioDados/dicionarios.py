''' 
Um dicionário é um conjunto não-ordenado de pares chave: valor,
onde as chaves são únicas em uma dada instância do dicionário.
Dicionários são delimitados por chaves: {}, e contem uma lista de
pares chave: valor separada por vírgulas.
'''

pessoa = {"Nome": "Guilherme", "Idade": 28}

pessoa = dict(nome = "Guilherme", idade = 28)

pessoa["telefone"] = "222-2121" # Adiciona em pessoa

# Acesso aos dados
pessoa["nome"]
pessoa["idade"]
pessoa["telefone"]

pessoa["nome"] = "Maria"
pessoa["idade"] = 19
pessoa["telefone"] = "920121-92102"

# Dicionários aninhados

pessoas = {
    "guilherme@gmail.com": {"nome": "Guilherme"},
    "giovanna@gmail.com": {"nome": "Giovanna"},
    "chappie@gmail.com": {"nome": "Chappie"},
    "melanie@gmail.com": {"nome": "Melanie", "extra": {"A": 1} },
}

nome = pessoas["giovanna@gmail.com"]["nome"]

extra = pessoas["melanie@gmail.com"]["extra"]["A"]


# Iterar dicionario

for chave in pessoas:
    print(chave, pessoas[chave])

for chave, valor in pessoas.items():
    print(chave, valor)