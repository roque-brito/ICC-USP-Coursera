from time import sleep
from time import ctime
print('-'*30)
print(f'Iniciando... {ctime()}')

def main():
    planeta3 = Planetas('Terra', 1, 1, 1, 1, 1)
    planeta4 = Planetas('Marte', 1.8, 0.53, 1.53, 2, 0.38)
    
    # posição na memoria:
    print(f'planeta3: {planeta3}')
    print(f'planeta4: {planeta4}')


sleep( 2 )

class Planetas:
    def __init__(self, nome, orbita, diametro, distanciaSol, moons, gravidade):
        self.nome = nome
        self.orbita = orbita
        self.diametro = diametro
        self.distanciaSol = distanciaSol
        self.moons = moons
        self.gravidade = gravidade 

    def imprima(self):
        print(f''''
        Planeta: {nome} | Revolução: {orbita} dias | Diametro: {diametro} Terra(s) | Luas: {moons} | Gravidade: {gravidade}
        
               '''
        
             )
    

main()

print(f'Terminou... {ctime()}')
print('-'*30)