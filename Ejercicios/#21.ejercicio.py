# 31 MARCO DE PALABRAS
"""
* Crea una función que reciba un texto y muestre cada palabra en una línea,
* formando un marco rectangular de asteriscos.
* - ¿Qué te parece el reto? Se vería así:
*   **********
*   * ¿Qué   *
*   * te     *
*   * parece *
*   * el     *
*   * reto?  *
*   **********
"""

def palabra_linea(cadena: str):
    cadena =  cadena.split()
    tem = []
    mayor = 0
    for i in cadena:
        tem.append(len(i) + 4)
    mayor = max(tem)
    print('*' * mayor)
    j = 0
    for i in cadena:
        print("* " + i  + " " * (mayor - tem[j]) + " *")
        j += 1 
    print('*' * mayor)


palabra_linea("¿Qué te parecera el reto neto?")