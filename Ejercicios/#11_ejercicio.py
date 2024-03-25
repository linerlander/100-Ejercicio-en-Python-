""" 
* Crea una función que transforme grados Celsius en Fahrenheit
* y viceversa.
*
* - Para que un dato de entrada sea correcto debe poseer un símbolo "°"
*   y su unidad ("C" o "F").
* - En caso contrario retornará un error.
""" 


def Fahrenheit_to(grado_celsius):
    Conversión = ((grado_celsius) * (9/5)) + 32
    return print(Conversión)

def Celsius_to(grado_fahrenheit):
    Conversión = (grado_fahrenheit - 32) *(5/9)  
    return print(Conversión)

def main():
    while True:
        print('### Conversión de grados ###')
        print('\n1. Celsius')
        print('2. Fahrenheit')
        print('3. Salir')
        optión = input('\nSeleccione la escala  de temperatura: ')

        if optión == '1':
            grado_celsius = float(input('\nIngrese la temperatura celsius para convertir a fahrenheit: '))
            Fahrenheit_to(grado_celsius)
        elif optión == '2':
            grado_fahrenheit =  float(input('\nIngrese la temperatura fahrenheit para convertir a celsius: '))
            Celsius_to(grado_fahrenheit)
        elif optión == '3':
            break
        else:
            print('\n¡Error, Ingrese una opción válida!')
main()