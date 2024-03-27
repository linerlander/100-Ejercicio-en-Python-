# 23 CONJUNTOS
"""
* Crea una función que reciba dos array, un booleano y retorne un array.
* - Si el booleano es verdadero buscará y retornará los elementos comunes
*   de los dos array.
* - Si el booleano es falso buscará y retornará los elementos no comunes
*   de los dos array.
* - No se pueden utilizar operaciones del lenguaje que
*   lo resuelvan directamente.
"""

def conjuntos(lista1: list, lista2: list, valor: bool)-> list:
    if valor == True:
        temp = []
        for i in range(len(lista1)):
            for j in range(len(lista2)):
                if lista2[j] == lista1[i]:
                    temp.append(lista2[j])
        return list(set(temp))
    elif valor == False:
        temp = lista1 + lista2
        temp2 = []
        for i in range(len(temp)):
            if temp.count(temp[i]) < 2:
                temp2.append(temp[i])
        return temp2
lista1 = [4,5,60,8,5,9]
lista2 = [4,5,10,8,9,5]
print(conjuntos(lista1,lista2,True))
print(conjuntos(lista1,lista2,False)) 
