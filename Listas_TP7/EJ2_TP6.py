#Calcular la suma de los números de la lista.

def guardarenlista (A,B):
    listanumeros = []
    mayor = A
    menor = B

    if A > B:
        mayor = A
        menor = B
    else:
        mayor = B
        menor = A

    numero = int(input(f"Ingrese un numero entre {menor} y {mayor}, para finalizar la carga ingrese -1: "))

    while numero != -1:
        while numero < menor or numero > mayor:
            numero = int(input("Ingresaste un numero fuera del rango, por favor, volve a intentarlo: "))
        listanumeros.append(numero)
        numero = int(input(f"Ingrese un numero entre {menor} y {mayor}, para finalizar la carga ingrese -1: "))
    
    print ("La carga de numeros finalizo")
    return listanumeros

def sumarnumeroslista(listanumeros):
    numero = 0
    for i in listanumeros:
        numero = i + numero
    return numero

listanumeros = guardarenlista(5,8)
suma = sumarnumeroslista(listanumeros)
print (f"La suma de los numeros de la lista es {suma}")

