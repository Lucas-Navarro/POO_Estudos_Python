# Tupla é irmão da lista, só que é mais restrita
# Tupla é uma estrutura imutável

# São compreendidas com parenteses ao inves de []
frutas = ("laranja", "pera", "uva",)  # sempre virgula no final para não bugar

letras = tuple("PyThon")

numeros = tuple([1,2,3,4])

pais = ("Brasil",) # uso , no final para entender que é um item só

# Acesso Direto Tupla

frutas[0] # laranja
frutas[-1] # uva

# Tuplas aninhadas ( Tabelas )

matriz = (
    (1, "a", 2),
    ("b", 2, 3),
    (6, 5, 4),
)

