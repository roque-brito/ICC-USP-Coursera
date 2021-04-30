# chamada de funções:
def main():
    t1 = Triangulo(2, 3, 5)
    t2 = Triangulo(4, 6, 10)

    x = t1.semelhantes(t2)
    print(f'Os triângulos são semelhantes: {x}')

class Triangulo:
    
    # criando um "construtor de classe" para os lados do triângulo - atributos são os lados triângulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # criando uma função - método - para testar a smilaridade dos triangulos t1 e t2:
    def semelhantes(self, t2):
        triangulo1 = [self.a, self.b, self.c]
        
        # para criar atributos: nome_do_objeto.nome_do_atributo
        if (self.a / t2.a) == (self.b / t2.b) and (self.a / t2.a) == (self.c / t2.c):
            return True
        
        else:
            return False
            
main()