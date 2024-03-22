"""
* Crea una única función (importante que sólo sea una) que sea capaz
* de calcular y retornar el área de un polígono.
* - La función recibirá por parámetro sólo UN polígono a la vez.
* - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
* - Imprime el cálculo del área de un polígono de cada tipo.
"""

def area_polígono():
    while True:
        print('### Área de un Polígono ###')
        print('\n1. Triángulo')
        print('2. Cuadrado')
        print('3. Rectángulo')
        print('4. Salir')

        opción = input('\n Elija una opción de Polígono: ')
        match opción:
            case '1':
                base = input('Cual es la base del triángulo: ')
                if base.isdigit():
                    altura = input('Cual es la altura del triángulo: ')
                    if altura.isdigit():
                        área = (int(base) * int(altura))/2
                        print(f'El área del triángulo con base {base} y altura {altura} es {área}')
                    else:
                        print('\n¡¡n¡¡Error inserte un número correcto de altura!!')
                        break
                else:
                    print('\n¡¡Error inserte un número correo de base!!')
                    break
            case '2':
                lado =  input('Cual es lado del cuadrado: ')
                if lado.isdigit():
                    área = int(lado) * int(lado)
                    print(f'El área del cuadrado con lado {lado} es {área}')
                else:
                    print('\n¡¡Error inserte un número correcto de lado!!')
                    break
                
            case '3':
                base =  input('Cual es la base del rectangulo: ')
                if base.isdigit():
                    altura =  input('Cual es la altura del rectangulo:')
                    if altura.isdigit():
                        área = int(base) * int(altura)
                        print(f'El área del rectangulo con base {base} y altura {altura} es {área}')
                    else:
                        print('\n¡¡Error inserte un número correcto de altura!!')
                        break
                else:
                    print('\n¡¡Error inserte un número correcto de base!!')
                    break
            case '4':
                break
        
area_polígono()