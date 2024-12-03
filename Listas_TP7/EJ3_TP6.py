#Determinar si la lista es capicúa (palíndromo). Una lista capicúa se lee de igual 
#modo de izquierda a derecha y de derecha a izquierda. Por ejemplo, [2, 7, 7, 2] 
#es capicúa, mientras que [2, 7, 5, 2] no lo es.

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

lista = guardarenlista (1,8)

def espalindromo (lista):
    inicio = 0
    fin = len(lista) - 1

    while inicio < fin:
        if lista[inicio] != lista[fin]:
            return False
        else:
            inicio =  inicio + 1
            fin = fin -1
    return True

if espalindromo (lista):
    print("Es palindromo")
else:
    print("No es palindromo")
