#confeccionar una agenda. utilizar un diccionario cuya clave sea la fecha.
#permitir almacenar distintas actividades para la misma fecha (se ingresa la hora y la actividad)
#implementar las siguientes funciones:
#1) carga de datos en la agenda
#2) listado completo de la agenda
#3) consulta de una fecha.

def cargar():
    agenda={}
    continua1="s"
    while continua1=="s":
        fecha=input("ingrese la fecha con formato dd/mm/aa:")
        continua2="s"
        lista=[]
        while continua2=="s":
            hora=input("ingrese la hora de la actividad con formato hh:mm ")
            actividad=input("ingrese la descripcion de la actiidad")
            lista.append((hora, actividad))
            continua2=input("ingresa otra actividad para la misma fecha[s/n]:")
        agenda[fecha]=lista
        continua1=input("ingresa otra fecha[s/n]:")
    return agenda

def imprimir(agenda):
    print("listado completa de la agenda")
    for fecha in agenda:
        print("para la fecha: ", fecha)
        for hora,actividad in agenda[fecha]:
            print(hora,actividad)

def consulta_fecha(agenda):
    fecha=input("Ingrese la fecha que desea consultar:")
    if fecha in agenda:
        for hora,actividad in agenda[fecha]:
            print(hora,actividad)
    else:
        print("No hay actividades agendadas para dicha fecha")

#bloque principal
agenda=cargar()
imprimir(agenda)
consulta_fecha(agenda)
