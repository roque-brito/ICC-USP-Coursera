
class Triangulo:
    
    # criando um construtor para os lados do triângulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # criando o método para calcular o perímetro: 
    def perimetro(self):
        
        p = self.a + self.b + self.c

        return p

t = Triangulo(1,1,1)
     


