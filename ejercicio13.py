#desarrollar una aplicacion que nos permita crear un diccionario
#ingles/castellaño. La clave es la palabra en ingles y el valor
#es la palabra en castellano
#1) cargar el diccionario
#2) listado completo del diccionario
#3) ingresar por teclado una palabra en ingles y si existe en el diccionario

def cargar():
    diccionario={}
    continua="s"
    while continua=="s":
        caste=input("ingrese palabra en castellano")
        ing=input("ingrese palabra en ingles:")
        diccionario[ing]=caste
        continua=input("quiere cargar otra palabra:[s/n]")
    return diccionario

def imprimir(diccionario):
    print("Listado completo del diccionario")
    for ingles in diccionario:
        print(ingles,diccionario[ingles])


def consulta_palabra(diccionario):
    pal=input("Ingrese la palabra en ingles a consultar:")
    if pal in diccionario:
        print("En castellano significa", diccionario[pal])


#bloque principal

diccionario=cargar()
imprimir(diccionario)
consulta_palabra(diccionario)
