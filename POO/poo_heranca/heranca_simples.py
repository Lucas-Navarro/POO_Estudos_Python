class Veiculo:
    def __init__(self, cor, placa, num_rodas):
        self.cor = cor
        self.placa = placa
        self.num_rodas = num_rodas

    def ligar_motor(self):
        print('Ligando motor')

    def __str__(self):
        return self.cor

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, num_rodas, carregado):
        super().__init__(cor, placa, num_rodas)
        self.carregado = carregado

    def levando_carga(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

moto = Motocicleta('cinza', 'LPASAPL123', 2)
moto.ligar_motor()

carro = Carro('Preto', 'XDXD123', 4)
carro.ligar_motor()

caminhao = Caminhao('Branco', 'FOAD2103', 8, 'Sim')
caminhao.ligar_motor()
caminhao.levando_carga()
print(caminhao)