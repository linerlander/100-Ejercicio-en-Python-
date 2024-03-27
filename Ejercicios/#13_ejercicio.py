#15 ¿ES UN NÚMERO DE ARMSTRONG?
"""
* Escribe una función que calcule si un número dado es un número de Armstrong
* (o también llamado narcisista).
* Si no conoces qué es un número de Armstrong, debes buscar información
* al respecto.
"""

def armstrong(num):
    valor = 0
    armstrong = False
    for i in range(len(num)):
        valor = valor + int(num[i])** len(num) 
    num =  int(num)
    if valor == num:
        armstrong = True
        return armstrong
    return armstrong

print(armstrong("1634"))