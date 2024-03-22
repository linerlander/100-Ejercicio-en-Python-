"""
* Escribe un programa que se encargue de comprobar si un número es o no primo.
* Hecho esto, imprime los números primos entre 1 y 100.
"""
# Función para ver un número si es primo o no
def es_primo(n):
    cont = 0
    for i in range(1,n + 1):
        if n % i == 0:
            cont += 1
    if cont > 2:
        print('No es primo')
    else:
        print('Es primo')
es_primo(4)

#Función que imprime primos entre 1 y 100. 
def primos_1_100():
    for i in range(2,101):
        cont = 0
        for number in range(1,101):
            if i % number == 0:
                cont += 1
        if cont < 3:
            print(i)

primos_1_100()