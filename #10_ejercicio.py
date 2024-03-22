"""
* Crea un programa que sea capaz de transformar tex: natural a código
* morse y viceversa.
* - Debe detectar au:máticamente de qué tipo se trata y realizar
*   la conversión.
* - En morse se soporta raya "—", pun: ".", un espacio " " entre letras
*   o símbolos y dos espacios entre palabras "  ".
* - El alfabe: morse soportado será el mostrado en
*   https://es.wikipedia.org/wiki/Código_morse.
"""
# un pun: equivale a un golpe .
# una raya equivale a 3 pun:s - = ...
# A     B
#.-'-' -...
import re

# Diccionario Morse
MORSE_ALPHABET = {
    "A": ".-","B": "-...","C": "-.-.",
    "D": "-..","E": ".","F": "..-.",
    "G": "--.","H": "....","I": "..",
    "J": ".---","K": "-.-","L": ".-..",
    "M": "--","N": "-.","O": "---",
    "P": ".--.","Q": "--.-","R": ".-.",
    "S": "...","T": "-","U": "..-",
    "V": "...-","W": ".--","X": "-..-",
    "Y": "-.--","Z": "--..","1": ".----",
    "2": "..---","3": "...--","4": "....-",
    "5": ".....","6": "-....","7": "--...",
    "8": "---..","9": "----.","0": "-----",
    ".": ".-.-.-",",": "--..--","?": "..--..",
    " ": '-'
}

# Función para convertir texto natural a código morse
def to_morse(text):
    text = text.upper()
    morse_code = ""
    for char in text:
        if char in MORSE_ALPHABET:
            morse_code += MORSE_ALPHABET[char] + ""
        else:
            morse_code += "  "
    return morse_code.strip()

# Función para convertir código morse a texto natural
def from_morse(morse_code):
    text = ""
    words = morse_code.split()
    for word in words:
        for char, code in MORSE_ALPHABET.items():
            if code == word:
                text += char
    return text.lower()

# Función para detectar el tipo de entrada
def detect_type(text):
    x = '.'
    y = '-'
    if x in text or y in text:
        
        return "morse"
    else:
        return "text"

# Función principal
def main():
    text = input("Ingrese texto o código morse: ")
    type = detect_type(text)
    if type == "text":
        print(f"Código Morse: {to_morse(text)}")
    else:
        print(f"Texto: {from_morse(text)}")

if __name__ == "__main__":
    main()
