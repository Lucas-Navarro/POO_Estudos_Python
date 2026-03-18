frutas = ["laranja", "maçã", "uva"]
print(frutas)

fruta = []
print(fruta)


# Construtor list
letras = list("PYTHON") # Vai fazer uma lista com cada caracter sendo parte da lista
print(letras)


numeros = list(range(10)) # Vai fazer uma lista de 0 a 9
print(numeros)


carro = ["Ferrari", "F8", 42000, 2020, 2900, "São Paulo", True]
print(carro)

# Acesso direto = Acessar um objeto dentro da Array / Lista

print(frutas[1])
print(frutas[-1]) # Inverte da direita para esquerda, iniciando em -1

# Listas Aninhadas
# Estrutura em Matriz ( Tabelas ) 
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0]) # Pega apenas a linha
print(matriz[0][0]) # Pega o item da primeira linha e primeira coluna
print(matriz[0][-1]) # Vai até a primeira lista e pega o ultimo item
print(matriz[1][-1]) # Vai até a segunda lista e pega o ultimo item

# Fatiamento em Arrays

print(letras[0:]) # Vai até o final
print(letras[0:2]) # Determinou até onde vai
print(letras[:2]) # Vai de 2 para trás
print(letras[::-1])

# Função Enumerate

carros = ["gol", "celta", "palio"]

# Compreensão de listas = Filtros

# Versão 1 
numeros = [1, 30, 32, 21, 2, 9, 54, 302]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

# Versão 2
npares = [numero for numero in numeros if numero % 2 == 0]

# Modificando Valores versão 1
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

# Modificando Valores versão 2
nquadrado = [numero ** 2 for numero in numeros]