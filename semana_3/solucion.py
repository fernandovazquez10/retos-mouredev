import random


class PasswordGenerator:

    def __init__(self, longitud:int=8, con_mayusculas: bool = False, 
                con_numeros: bool=False, con_simbolos: bool = False):
        if longitud < 8 or longitud > 16:
            raise "La longitud debe ser de entre 8 y 16"
        self.longitud = longitud
        self.con_mayusculas = con_mayusculas
        self.con_numeros = con_numeros
        self.con_simbolos = con_simbolos

    def get_letras(self):
        letras = []
        for letra in 'abcdefghijklmnopqrstuvwxyz':
            letras.append(letra)
        return letras

    def get_simbolos(self):
        simbolos = []
        for simbolo in "!#$%&/()=?-.,@":
            simbolos.append(simbolo)
        return simbolos

    def get_numeros(self):
        numeros = []
        for numero in range(0,10,1):
            numeros.append(numero)
        return numeros

    def new_password(self):
        password = []
        longitud = 0
        letras = self.get_letras()
        random.shuffle(letras)
        composicion = [letras]
        if self.con_mayusculas:
            letras_mayusculas = [] 
            for letra in letras:
                letras_mayusculas.append(letra.upper())
            random.shuffle(letras_mayusculas)
            composicion.append(letras_mayusculas)
        
        if self.con_numeros:
            numeros = self.get_numeros()
            random.shuffle(numeros)
            composicion.append(numeros)

        if self.con_simbolos:
            simbolos = self.get_simbolos()
            random.shuffle(simbolos)
            composicion.append(simbolos)

        while longitud != self.longitud:
            for compositor in composicion:
                caracter = random.choice(compositor)
                password.append(str(caracter))
                longitud += 1
                if longitud == self.longitud:
                    break

        random.shuffle(password)
        password = "".join(password)
        return password 


new_password = PasswordGenerator(
    longitud=10,
    con_mayusculas=True,
    con_numeros=True,
    con_simbolos=True
).new_password()
print(new_password)
