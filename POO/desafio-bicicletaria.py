class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor 
        self.aro = 18
        self.marcha = 1

    def buzinar(self):
        print("BIIIIIIIIIIIIIIIII")

    def parar(self):
        print("Parando a bicicleta")
        print("Bicicleta parada")
        
    def correr(self):
        print("Acelerando a bicicleta")
        print("Correndo")

    def trocar_marcha(self, nro_marcha):
        print("Trocando marcha")
        
        def _trocar_marcha(nro_marcha):
            if nro_marcha > self.marcha:
                print('Marcha trocada')   
            else:
                print("Não foi possivel trocar a marcha")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f' {chave}={valor}' for chave, valor in  self.__dict__.items()])}"



b1 = Bicicleta("Amarela", "Caloi EX", 2024, 1200)
b1.buzinar()
b1.parar()
b1.correr()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("Roxo", "Monark", 2010, 2000)
Bicicleta.buzinar(b2) # igual b1.buzinar 
print(b2)
