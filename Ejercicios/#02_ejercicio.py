"""
* Escribe una función que reciba dos palabras (String) y retorne
* verdadero o falso (Bool) según sean o no anagramas.
* - Un Anagrama consiste en formar una palabra reordenando TODAS
*   las letras de otra palabra inicial.
* - NO hace falta comprobar que ambas palabras existan.
* - Dos palabras exactamente iguales no son anagrama.
"""


def anagrama(text_1, text_2) -> bool:
    text_1 = text_1.lower()
    text_2 = text_2.lower()
    lista_1 = []
    lista_2 = []
    for i in text_1:
       lista_1.append(i)
    for n in text_2:
       lista_2.append(n)
    lista_1.sort()
    lista_2.sort()

    if lista_1 == lista_2:
       return True
    else:
       return False
     
x = anagrama('maro','roma')
print(x)

