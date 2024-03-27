# 17 EN MAYÚSCULA
""" 
* Crea una función que reciba un String de cualquier tipo y se encargue de
* poner en mayúscula la primera letra de cada palabra.
* - No se pueden utilizar operaciones del lenguaje que
*   lo resuelvan directamente.
"""

def mayúscula(word: str)-> str:
    palabra = {'a': 'A', 'b': 'B', 'c': 'C',
               'd': 'D', 'e': 'E', 'f': 'F', 
               'g': 'G', 'h': 'H', 'i': 'I', 
               'j': 'J', 'k': 'K', 'l': 'L', 
               'm': 'M', 'n': 'N', 'o': 'O', 
               'p': 'P', 'q': 'Q', 'r': 'R', 
               's': 'S', 't': 'T', 'u': 'U', 
               'v': 'V', 'w': 'W', 'x': 'X', 
               'y': 'Y', 'z': 'Z'}
    for words in palabra:
        if words == word[0]:
            word = palabra[words] + word[1:]
    return word

print(mayúscula("lander es lander"))

