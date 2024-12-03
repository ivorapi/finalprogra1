#Obtener el dígito central de un número entero pasado como parámetro, sólo si la 
#cantidad de dígitos es impar. Si la longitud fuera par devolver -1. Ejemplo: 
#digitocentral(12345) devuelve 3, y digitocentral(123456) devuelve -1


def esimpar(numeroentero):
    numeroentero = str (numeroentero)
    if len(numeroentero)%2 == 0:
        return False
    return True
    


def digitocentral(numero):
    if esimpar(numero) == True:
        numero = str(numero)
        posicionmedio = len(numero) // 2 
        return numero[posicionmedio]
    else:
        return -1
         
        
print (digitocentral(1234))