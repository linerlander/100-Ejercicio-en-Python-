# 30 ORDENA LA LISTA
"""
* Crea una función que ordene y retorne una matriz de números.
* - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro
*   adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor
*   o de mayor a menor.
* - No se pueden utilizar funciones propias del lenguaje que lo resuelvan
*   automáticamente.
"""

def ordenamiento(lista, cadena):
    while True:
        tem = 0
        if cadena == "Asc":
            for i in range(len(lista)):
                for j in range(len(lista)-1):
                    if lista[j] > lista[j + 1]:
                       tem =  lista[j]
                       lista[j] = lista[j + 1] 
                       lista[j + 1] = tem

            return lista
        elif cadena == "Desc":
            for i in range(len(lista)):
                for j in range(len(lista)-1):
                    if lista[j] < lista[j + 1]:
                        tem =  lista[j]
                        lista[j] = lista[j + 1] 
                        lista[j + 1] = tem
            return lista
        else:
            break

lista = [20, 41, 6, 8, 90]
print(ordenamiento(lista,"Desc"))
print(ordenamiento(lista,"Asc"))
