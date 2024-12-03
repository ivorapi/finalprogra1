# Escribir la función comparar(a, b) que reciba como parámetros dos números en
#teros y devuelva 1 si el primero es mayor que el segundo, 0 si son iguales o -1 si 
#el primero es menor que el segundo. En este ejercicio debe aprovecharse la fun
#ción del ejercicio anterior. Ejemplo: comparar(4, 2) devuelve 1, y comparar(2, 4) 
#devuelve -1.

def signo (n):
    if n > 0:
        return  1
    else:
       if n < 0:
        return -1
       else:
          return 0
       
def comparar (a,b):
   resultado = a - b
   return signo(resultado)

print(comparar(2,2))