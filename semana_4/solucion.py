class QueSos:
    
    def __init__(self, numero:int):
        self.numero = numero
        self.es_fibonacci = False
        self.es_par = False
        self.es_primo = False
        self.comprobar_fibonacci()
        self.comprobar_par()
        self.comprobar_primo()
    
    def gen_fibonacci(self):
        n_1 =0
        n_2 =1
        c = -1
        while True:
            c +=1
            if c == 0:
                yield n_1
            elif c ==1:
                yield n_2
            else:
                aux = n_1 + n_2
                n_1 = n_2
                n_2 = aux
                yield aux

    def comprobar_fibonacci(self):
        for i in self.gen_fibonacci():
            if i == self.numero:
                self.es_fibonacci = True
            elif i > self.numero:
                break
    
    def comprobar_primo(self, n=2):
        if n >= self.numero:
            self.es_primo =  True
        elif self.numero % n != 0:
            self.es_primo(self, n + 1)
    
    def comprobar_par(self):
        if self.numero % 2 == 0:
            self.es_par = True

    def display(self):
        primo = "no es primo"
        if self.es_primo:
            primo = "es primo"
        fib = "no es fibonacci"
        if self.es_fibonacci:
            fib = "fibonacci"
        par = "no es par"
        if self.es_par:
            par = "es par"
        display = f"{self.numero} {primo}, {fib} y {par}"
        return display

print(QueSos(2).display())