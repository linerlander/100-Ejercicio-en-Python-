"""
* Crea un programa se encargue de transformar un número
* decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
"""


def tranformar_decimal(x):
    lista = []
    while True:
        a = x % 2
        x = x // 2
        lista.insert(0,a)
        if x == 2:
            a = x % 2
            x = x / 2
            lista.insert(0,a)
            lista.insert(0,x)
            break
        elif x == 1:
            a = x % 2
            lista.insert(0,a)
            break
    for i in lista:
        print(int(i),end=' ')
tranformar_decimal(8000)
