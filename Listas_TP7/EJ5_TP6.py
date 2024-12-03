#Desarrollar una función que reciba la lista como parámetro y devuelva una nueva 
#lista con los mismos elementos de la primera, pero en orden inverso. Por 
#ejemplo, si la función recibe [5, 7, 1] debe devolver [1, 7, 5].

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

def invertir (lista):
    listainvertida = []
    numero = 0
    for i in range(len(lista) -1, -1, -1):
        numero = lista [i]
        listainvertida.append(numero)
    return listainvertida

lista = guardarenlista (1,5)
listainvertida = invertir(lista)

print (lista)
print (listainvertida)


    