"""
* Crea un programa que cuente cuantas veces se repite cada palabra
* y que muestre el recuento final de todas ellas.
* - Los signos de puntuación no forman parte de la palabra.
* - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
* - No se pueden utilizar funciones propias del lenguaje que
*   lo resuelvan automáticamente.
"""

def conteo_palabra(text):
    text = text.lower().split(' ')
    dic = {}
    for palabra in text:
        cont = 0
        for n in text:
            if n == palabra:
                cont += 1
        dic[palabra] = cont
    print(dic)

conteo_palabra('cual es la palabra y cual es los número')