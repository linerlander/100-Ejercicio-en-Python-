"""
* Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno).
* ¿De cuántas maneras eres capaz de hacerlo?
* Crea el código para cada una de ellas.
"""

def main():
    print("**** 1 ****")
    for i in range(1,101):
        print(i)

    print("**** 2 ****")
    num = 1
    while True:
        if num > 0  and num < 101:
            print(num)
            num += 1
        else:
            break
        
    print("**** 3 ****")
    def recursivo(number):
        if number > 0 and number < 101:
            print(number)
            recursivo(number + 1)
    recursivo(1)
    print("**** 4 ****")
   

main()

