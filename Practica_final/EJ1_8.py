#Leer los números de legajo de los alumnos de un curso y su nota de examen 
#final. El fin de la carga se determina ingresando un -1 como legajo. Se debe vali
#dar que la nota ingresada esté entre 1 y 10. Terminada la lectura de datos, in
#formar:

#Cantidad de alumnos que aprobaron con nota mayor o igual a 4
#Cantidad de alumnos que desaprobaron el examen. Nota menor a 4
#Promedio de nota y los legajos que superan el promedio
#Luego se solicita mostrar un listado de legajos y calificaciones ordenado de manera ascendente según el número de legajo. Resolver de dos formas: Utilizando 
#dos listas paralelas

def definirnotas ():
    listalegajo = []
    listanota = []
    legajo = int(input("Ingrese un numero de legajo, para finalizar la carga ingrese -1: "))
    while legajo != -1:
        listalegajo.append(legajo) 
        nota = int(input("Ingrese un numero entre 1 y 10: "))
        while nota < 1 or nota > 10:
            nota = int(input("Ingresaste un numero fuera de rango, por favor, ingrese un numero entre 1 y 10: "))
        listanota.append(nota)
        legajo = int(input("Ingrese un numero de legajo, para finalizar la carga ingrese -1: "))
    print("La carga de datos finalizo")
    
    print(listalegajo,listanota)
    print(aprobados(listanota))
    print(promedio (listanota, listalegajo))
    


def aprobados(listanota):
    aprobados = 0
    desaprobados = 0

    for i in listanota:
        if i >= 4:
            aprobados = aprobados + 1
        else:
            desaprobados = desaprobados + 1
    return aprobados, desaprobados

def promedio (listanota, listalegajo):
    promedioaux = 0
    listamayorpromedio = []
    
    for i in listanota:
        promedioaux = promedioaux + i
    promedios = promedioaux / len(listanota)

    for i in range(len(listanota)):
            if listanota [i] > promedios:
                listamayorpromedio.append (listalegajo [i])

    return promedios, listamayorpromedio

definirnotas ()

