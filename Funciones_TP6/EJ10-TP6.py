#Extraer un dígito de un número. La función recibe como parámetros dos números 
#enteros, uno será del que se extraiga el dígito y el otro indica qué cifra se desea 
#obtener. La cifra de la derecha se considera la número 0. Retornar el valor -1 si 
#no existe el dígito solicitado. Tener en cuenta que el número puede ser positivo o 
#negativo. Ejemplo: extraerdigito(12345, 1) devuelve 4, y extraerdigito(12345, 8) 
#devuelve -1.

def invertironline (palabra):
    palabrainvertida = " "
    for letra in palabra:
        palabrainvertida = letra + palabrainvertida
    return palabrainvertida


def extraer (numero,posicion):
    numeroinvertido = invertironline (str(numero))
    if posicion < len(numeroinvertido):
        for i in range(len(numeroinvertido)):
            if i == posicion:
                return numeroinvertido[i]
    else:
        return -1


print (extraer(12345,10))