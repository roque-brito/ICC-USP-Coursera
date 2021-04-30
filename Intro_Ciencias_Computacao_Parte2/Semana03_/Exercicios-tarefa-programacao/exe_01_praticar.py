class Triangulo:
    
    # criando um construtor para os lados do triângulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def retangulo(self):
        if self.a > self.b and self.a > self.c:
            h  = self.a ** 2
            co = self.b ** 2
            ca = self.c ** 2

            if h == (co + ca):
                return True # se for retângulo
            else:
                return False # não-retângulo
        
        
        elif self.b > self.a and self.b > self.c:
            h  = self.b ** 2
            co = self.a ** 2
            ca = self.c ** 2

            if h == (co + ca):
                return True # se for retângulo
            else:
                return False # não-retângulo
        
        
        elif self.c > self.b and self.c > self.a:
            h  = self.c ** 2
            co = self.b ** 2
            ca = self.a ** 2

            if h == (co + ca):
                return True # se for retângulo
            else:
                return False # não-retângulo

        else:
            return False # não-retângulo
        

t = Triangulo(1, 2, 5)
print(t.retangulo())

u = Triangulo(3, 4, 5)
print(u.retangulo())
