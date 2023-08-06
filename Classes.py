class Clase: 
    def __init__(self, numero, palabra):
        self.numero = numero
        self.palabra = palabra
        self.a = numero**2
        self.b = numero**3
        self.c = 999
    def imprimir(self):
        print("Hola yo soy {0}.".format(self.palabra))
    def dime_datos(self):
        print("Con x=%i obtenemos; a=%i, b=%i, c=%i" % (self.numero, self.a, self.b, self.c))
    