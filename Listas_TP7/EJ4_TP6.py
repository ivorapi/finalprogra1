#Escribir una función para contar cuántas veces aparece un valor dentro de la 
#lista. La función recibe como parámetros la lista y el valor a buscar, y devuelve 
#un número entero

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
def buscador (lista,valorabuscar):
    contador = 0
    for i in lista:
        print(i)
        if valorabuscar == i: 
            contador = contador + 1
    return contador

lista = guardarenlista (1,10)
contador = buscador (lista,5)

print(contador)