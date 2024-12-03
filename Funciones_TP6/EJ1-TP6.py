# Escribir una función que reciba como parámetros dos números enteros. Calcular 
#y devolver el resultado de la multiplicación de ambos valores utilizando solamen
#te sumas. Por ejemplo 4 * 3 = 4 + 4 + 4 

def multiplicar(a, b):
    res = 0
    for (i) in range(b):
        res = res + a
        print (res)
    return res

print (multiplicar(4,3))
    

