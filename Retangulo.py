class Retangulo():
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura
    
    def perimetro(self):
        return ( 2 * (self.largura + self.altura))
    
    def diagonal(self):
        return (((self.largura ** 2) + (self.altura ** 2)) ** (1/2))



