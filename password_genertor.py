#este es un generador de contrasenas
import random

"""
2 uppercase letters from A to Z,
2 lowercase letters from a to z,
2 digits from 0 to 9,
2 punctuation signs such as !, ?, “, # etc.

"""


def main():
    password_divided = []
    for i in range(8):
        digito = generar_digito(i + 1)
        password_divided.append(digito)
    random.shuffle(password_divided)
    final_password = juntar_palabra(password_divided)
    
    print(final_password)
    

def juntar_palabra(lista):
    palabra = ""
    for i in range(len(lista)):
        palabra = palabra + lista[i]
    return palabra

def generar_digito(n):
    rango = []
    
    #uppercase letters
    if n in [1,2]:
        rango = [65,90]
    #lowecase
    if n in [3,4]:
        rango = [97,122]
    #digits from 0 to 9
    if n in [5,6]:
        rango = [48,57]
    #punctuation signs such as !, ?, “, # etc.
    if n in [7,8]:
        rango = [33,47]
    
    numero = random.randint(rango[0],rango[1])
    return chr(numero)

if __name__ == "__main__":
    main()