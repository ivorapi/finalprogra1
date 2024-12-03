# Dados dos parámetros enteros A y B, obtener AB (A elevado a la B) mediante 
#multiplicaciones sucesivas, utilizando la función del ejercicio anterior para multi plicar. Por ejemplo 43 = 4 * 4 * 4

def multiplicar (a,b):
    res = 0
    for (i) in range (b):
        res += a
    return res

def elevar (a,b):
    res = 1
    for (i) in range (b):
        res = multiplicar (res,a)
    return res

print (elevar (2,5))