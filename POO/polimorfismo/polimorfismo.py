class Passaro:
    def voar(self):
        pass

class Pardal(Passaro):
    def voar(self):
        print('Pardal Vooa')

class Avestruz(Passaro):
    def voar(self):
        print('Avestruz não vooa')

def plano_voo(passaro):
    passaro.voar()

plano_voo(Pardal())
plano_voo(Avestruz())