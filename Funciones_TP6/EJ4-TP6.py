#Devolver True si el número entero recibido como primer parámetro es múltiplo 
#del segundo, o False en caso contrario. Ejemplo: esmultiplo(40, 8) devuelve True y esmultiplo(50, 3) devuelve False

def esmultiplo (a,b):
    if a % b == 0:
        return True
    else:
        return False
print (esmultiplo(40,8))    