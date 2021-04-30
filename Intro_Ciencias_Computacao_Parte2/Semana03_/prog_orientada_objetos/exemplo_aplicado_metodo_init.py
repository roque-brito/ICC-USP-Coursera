def main():
    carro1 = Carro('brasília', 1969, 'amarela', 80)
    carro2 = Carro('fuscão', 1981, 'preto', 95)

    carro1.acelere(40)
    carro2.acelere(50)
    carro1.acelere(80)
    carro1.pare()
    carro2.acelere(110)

class Carro:
    def __init__(self, m, a, c, vm):
        self.modelo = m
        self.ano    = a
        self.cor    = c
        self.vel    = 0
        self.maxV   = vm  # velocidade máxima

    def imprima(self):
        if self.vel == 0: # carro parado - da para ver o ano (ou a placa!)
            print(f'{self.modelo} {self.cor} {self.ano}')
        elif self.vel < self.maxV:
            print(f'{self.modelo} {self.cor} indo a {self.vel} km/h')
        else:
            print(f'{self.modelo} {self.cor} indo muuuito raaaapiiiidooo!')

    def acelere(self, v):
        self.vel = v
        if self.vel > self.maxV:
            self.vel = self.maxV
        self.imprima()

    def pare(self):
        self.vel = 0
        self.imprima()

main()
        
        
    
    
    
    
            
