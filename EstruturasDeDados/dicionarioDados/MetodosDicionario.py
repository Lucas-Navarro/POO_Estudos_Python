# .clear

# .copy
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "333-323"}
}

copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "GUI"}

# .fromkeys
# Cria um conjunto de chaves

dict.fromkeys(["nome", "telefone"])
dict.fromkeys(["nome", "telefone"], "vazio")

# .get
# Get procura a chave

contatos["chave"] # KeyError

contatos.get("chave") # None
contatos.get("chave", {}) # {}
contatos.get("guilherme@gmail.com", {})

# .items

contatos.items()

# .keys
# Ve chaves existentes 
contatos.keys()

# .pop
# Remove os itens
contatos.pop("guilherme@gmail.com")
contatos.pop("guilherme@gmail.com", {})

# .popITEM
# Remove um item das chaves do dicionario
contatos.popitem()

# .setDefault
# Não altera chaves existentes, só adiciona se não existir
contatos.setdefault("nome", "Giovanna")
contatos.setdefault("idade", 29)

# .update
# Atualiza os itens com outro dicionario
contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})

# .values
# Retorna só os valores das chaves
contatos.values()

# in
# Verifica se existe esta chave nos dicionarios
resultado = "guilherme@gmail.com" in contatos

resultado = "idade" in contatos["guilherme@gmail.com"]

# del
# Remove apenas chave ou chave inteira
del contatos["guilherme@gmail.com"]["nome"]
del contatos["guilherme@gmail.com"]