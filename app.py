#/*
 #* Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 #* Ejemplos:
 #* - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 #* - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 #*/
import math

def es_cuadrado_perfecto(numero):
    raiz_cuadrada = math.sqrt(numero)
    return raiz_cuadrada == int(raiz_cuadrada)

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def es_par(numero):
    return numero % 2 == 0

def verificar_propiedades(numero):
    es_numero_primo = es_primo(numero)
    es_cuadrado1 = 5 * numero**2 - 4
    es_cuadrado2 = 5 * numero**2 + 4
    cuadrado_perfecto = es_cuadrado_perfecto(es_cuadrado1) or es_cuadrado_perfecto(es_cuadrado2)
    es_numero_par = es_par(numero)

    if es_numero_primo and cuadrado_perfecto and es_numero_par:
        print(f"{numero} es primo, fibonacci y es par.")
    elif es_numero_primo and not cuadrado_perfecto and es_numero_par:
        print(f"{numero} es primo, no es fibonacci y es par.")
    elif es_numero_primo and cuadrado_perfecto and not es_numero_par:
        print(f"{numero} es primo, fibonacci y es impar.")
    elif es_numero_primo and not cuadrado_perfecto and not es_numero_par:
        print(f"{numero} es primo, no es fibonacci y es impar.")
    elif not es_numero_primo and cuadrado_perfecto and es_numero_par:
        print(f"{numero} no es primo,es fibonacci y es par")
    elif not es_numero_primo and  not cuadrado_perfecto and es_numero_par:
        print(f"{numero} no es primo,no es fibonacci y es par")
    else:
        print(f"{numero} no cumple todas las condiciones.")

# Ejemplos de uso
verificar_propiedades(2)
verificar_propiedades(7)

    