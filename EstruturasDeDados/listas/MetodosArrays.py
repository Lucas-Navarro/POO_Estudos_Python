# .append()
lista = []
lista.append(1)
lista.append("Python")
lista.append(["Lucas", 22, 69])

print(lista)

# .copy
l2 = lista.copy() 
print(lista)
print(lista)
print(id(l2), id(lista)) # o ID é diferente da original

l2[0] = 2
print(l2)
print(lista)

# .count
cores = ["vermelho", "azul", "verde", "azul"]
cores.count("vermelho") # 1
cores.count("azul") # 2
cores.count("verde") # 1

# .extend
linguagens = ["python", "js", "C"]
linguagens.extend(["java", "CSharp"])
print(linguagens)

# .index

linguagens.index("java") # 3
linguagens.index("python") # 0

# .pop
# Pop sempre vai tirando o ultimo elemento da lista como se fosse uma pilha de pratos
linguagens.pop() # CSharp
linguagens.pop() # java
linguagens.pop(0) # Pode especificar, como aqui vai tirar o Python

# .remove
# Ele apenas tira um dos elementos
linguagens.remove("js")


# .reverse
linguagens.reverse() # Inverte a ordem

# .sort
linguagens.sort() # Ordem alfabetica
linguagens.sort(reverse=True) # Vai inverter de volta
linguagens.sort(key=lambda x: len(x)) # Vai ordenar por tamanho menor para maior
linguagens.sort(key=lambda x: len(x), reverse=True) # Vai inverter por ordem de tamanho maior para o menor

# len
# Tamanho da lista, quantidade de elementos
len(linguagens)

# sorted
# mesma coisa que sort, só que é uma função
sorted(linguagens, key=lambda x:len(x)) # Ordena
sorted(linguagens, key=lambda x:len(x)) # Ordena do maior para menor

# .clear
lista.clear() 



