def guardarenlista ():
    listanumeros = []

    numero = int(input(f"Ingrese un numero para finalizar la carga ingrese -1: "))

    while numero != -1:
        listanumeros.append(numero)
        numero = int(input(f"Ingrese un numero para finalizar la carga ingrese -1: "))
    

    print ("La carga de numeros finalizo")
    return listanumeros

def burbujeo (lista):
    listaordenada = []
    while len(lista) != 0:
        mayor = lista [0]
        for i in lista:
            if i > mayor:
                mayor = i
        listaordenada.append(mayor)
        lista.remove(mayor)
            
    return listaordenada

lista = guardarenlista ()
print(lista)
listaordenada = burbujeo (lista)
print(listaordenada)