# 14 FACTORIAL RECURSIVO
"""
* Escribe una función que calcule y retorne el factorial de un número dado
* de forma recursiva.
"""
def factorial(number):
    if number == 0:
        return 1
    elif number == 1:
        return 1
    else:
        print(f'{number}')
        return number * factorial(number - 1)
print(factorial(5))



