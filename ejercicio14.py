#confeccionar un programa que permita cargar un codigo de producto como
#clave en un diccionario. Guardar para dicha clave el nombre del producto,
#Implementar las siguientes actividades:
#1 carga de datos en el diccionario.
#2 consulta de un producto por su clave, mostrar el nombre, precio y stock.
#4 listado de todos los productos que tengan un stock con valor cero.

def cargar():
    productos={}
    continua="s"
    while continua=="s":
        codigo=int(input("Ingrese el codugo del producto:"))
        descripcion=input("ingrese la descripcion:")
        precio=float(input("ingrese el precio:"))
        stock=int(input("ingrese el stock actual:"))
        productos[codigo]=(descripcion,precio,stock)
        continua=input("desea cargar otro producto[s/n]?")
    return productos

def imprimir(productos):
    print("listado completo de productos:")
    for codigo in productos:
        print(codigo,productos[codigo][0], productos[codigo][1],productos[codigo][2])


def consultar(productos):
    codigo=int(input("ingrese el codigo de articulo a consultar:"))
    if codigo in productos:
        print(productos[codigo][0], productos[codigo][1], productos[codigo][2])


def listado_stock_cero(productos):
    print("listado de articulos con stock en cero:")
    for codigo in productos:
        if productos[codigo][2]==0:
            print(codigo,productos[codigo][0],productos[codigo][1],productos[codigo][2])


#bloque principal

productos=cargar()
imprimir(productos)
listado_stock_cero(productos)
