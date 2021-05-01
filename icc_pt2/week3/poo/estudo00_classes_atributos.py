from time import sleep
from time import ctime
print('-'*40)
print(f'Iniciando... {ctime()}')

def main():
    # Parâmetros: (nome, órbita, diâmetro, distância-sol, satélites, gravidade): 
    planeta1 = Planetas('Mercúrio'  , 0.22, 0.37, 0.39, 0, 0.39)
    planeta2 = Planetas('Vênus'     , 0.67, 0.96, 0.72, 0, 0.89)
    planeta3 = Planetas('Terra'     , 1, 1, 1, 1, 1)
    planeta4 = Planetas('Marte'     , 1.8, 0.53, 1.53, 2, 0.38)
    planeta5 = Planetas('Jupiter'   , 11.86, 11.19, 5.19, 79, 2.35)
    planeta6 = Planetas('Saturno'   , 29.46, 9.41, 9.55, 82, 1.16)
    planeta7 = Planetas('Urano'     , 84.02, 4.00, 19.19, 27, 1.11)
    planeta8 = Planetas('Netuno'    , 165.00, 3.53, 30.03, 14, 1.38)

    lista_planetas = [
                      planeta1, planeta2, planeta3, planeta4, 
                      planeta5, planeta6, planeta7, planeta8
                     ]
    for i in range(len(lista_planetas)):
        planeta = lista_planetas[i]
        planeta.imprima()       
        sleep( 1.5 )

class Planetas:
    def __init__(self, nome, orbita, diametro, distanciaSol, moons, gravidade):
        self.nome = nome
        self.orbita = orbita
        self.diametro = diametro
        self.distanciaSol = distanciaSol
        self.moons = moons
        self.gravidade = gravidade 

    def imprima(self):
        print('-'*40)
        print(f' | Planeta: {self.nome} \n | Revolução: {self.orbita} dias \n | Diametro: {self.diametro} Terra(s) \n | Satélites naturais: {self.moons} \n | Gravidade: {self.gravidade}')   
        print('-'*40)
    
main()

print(f'Terminou... {ctime()}')
print('-'*40)