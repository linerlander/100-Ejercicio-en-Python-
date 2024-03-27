# 20 CONVERSOR TIEMPO
"""
* Crea una función que reciba días, horas, minutos y segundos (como enteros)
* y retorne su resultado en milisegundos.
"""

def conversión_tiempo(día:int, hora:int, minuto:int, segundo:int)-> int:
    cant_día = 86400000
    cant_hora = 3600000
    cant_minuto = 60000
    cant_segundo = 1000
 
    resultado = (día * cant_día) + (hora * cant_hora) + (minuto * cant_minuto) + (segundo * cant_segundo)
    return resultado

print(conversión_tiempo(2,2,2,2))
