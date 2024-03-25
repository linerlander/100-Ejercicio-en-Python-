""" 
*Crea un programa que analice dos palabras diferentes y realice comprobaciones
*para descrubir si son:
*-Palíndromos
*-Anagramas
*-Isogramas
""" 
def ana_iso_poli(word1, word2):
    # palíndromos
    print(f'¿{word1} es palíndromo? {word1 == word1[::-1]}')
    print(f'¿{word2} es palíndromo? {word2 == word2[::-1]}')

    # anagramas
    print(f'¿{word1} es anagrama de {word2}? {sorted(word1) == sorted(word2)}')

    # isogramas
    def isograma(word):
        aux = {}
        for elemento in word:
            aux[elemento] = aux.get(elemento,0) +1
        valor =  list(aux.values())
        elemento = valor[0]
        isograma = True
        for i in valor:
            if i != elemento:
                isograma = False
        return isograma
               
    print(f'¿{word1} es un isograma? {isograma(word1)}')
    print(f'¿{word2} es un isograma? {isograma(word2)}')

#ana_iso_poli("ana","rapar")
ana_iso_poli("amor","ramoa")