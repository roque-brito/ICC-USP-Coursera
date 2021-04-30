class Triangulo:
    
    # criando um construtor para os lados do triângulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # criando o método para comparar os lados do triângulo: 
    def tipo_lado(self):
        if self.a == self.b and self.a == self.c:
            return 'equilátero'
        
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return 'isósceles'
        
        else:
            return 'escaleno'

t = Triangulo(1,3,2)
