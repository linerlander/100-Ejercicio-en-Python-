"""
* Escribe un programa que imprima los 50 primeros números de la sucesión
* de Fibonacci empezando en 0.
* - La serie Fibonacci se compone por una sucesión de números en
*   la que el siguiente siempre es la suma de los dos anteriores.
*   0, 1, 1, 2, 3, 5, 8, 13...
"""

def Fibonacci():
    lista = [0,1]
    for i in range(0,50):
        valor = lista[len(lista)-1] + lista[len(lista)-2]
        lista.append(valor)
    print(lista)
Fibonacci()



