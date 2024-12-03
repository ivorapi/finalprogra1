#Escribir una función para ingresar desde el teclado una serie de números entre A 
#y B y guardarlos en una lista. En caso de ingresar un valor fuera de rango la fun
#ción mostrará un mensaje de error y solicitará un nuevo número. Para finalizar la 
#carga se deberá ingresar -1. La función recibe como parámetros los valores de A 
#y B, y devuelve la lista cargada (o vacía, si el usuario no ingresó nada) como 
#valor de retorno. Tener en cuenta que A puede ser mayor, menor o igual a B.


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


print(guardarenlista(5,8))