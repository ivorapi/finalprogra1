#Escribir una función que reciba como parámetros un número de día, un número 
#de mes y un número de año y devuelva la cantidad de días que faltan hasta fin 
#de mes. Luego desarrollar tres programas para: 
#·
# ·
# ·
#Ingresar una fecha formada por tres enteros (día, mes y año) e imprimir la cantidad de días que faltan hasta fin de año.
#Ingresar una fecha formada por tres enteros (día, mes y año) e imprimir la cantidad de días transcurridos en ese año hasta esa fecha.
#Ingresar dos fechas formadas por tres enteros (día, mes y año) e imprimir cuánto tiempo transcurrió entre ambas, expresando el resultado en 
#años, meses y días

def cuantofalta (dia):
    diasquefaltan = 30 - dia
    return diasquefaltan

def diashastaanio(dia,mes):
    diasquefaltananio = 365 - ((mes * 30) + cuantofalta(dia))
    return diasquefaltananio

def diastranscurridos (dia,mes):
    diastranscurridos = mes * 30 + dia
    return diastranscurridos

def diferenciafechas (dia1,mes1,anio1,dia2,mes2,anio2):
    anios = anio2 - anio1
    meses = mes2 - mes1
    dias = dia2 - dia1
          
    if dias < 0:
        meses -= 1
        dias += 30

    if meses < 0:
        anios -= 1
        meses += 12

    return anios, meses, dias

print (diferenciafechas (1,5,2019,1,1,2023))

## def es_bisiesto(anio):
    ##return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

##def dias_en_mes(mes, anio):
    ##if mes in [1, 3, 5, 7, 8, 10, 12]:
        ##return 31
    ##elif mes in [4, 6, 9, 11]:
       ## return 30
    ##elif mes == 2:
        ##return 29 if es_bisiesto(anio) else 28
    ##return 0