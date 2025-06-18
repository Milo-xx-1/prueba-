lista_productos= []
producto= {"nombre": nombre, "precio": precio, "cantidad": stock, "codigo": codigo }
#codigo tiene que tener 3 validaciones
#el codigo debe de tener un minimo de 5 caracteres
#el codigo debe tener al menos 2 mayusculas
#el codigo debe tener al menos 1 numero
opcion="0"

"""
sacar las funciones del while [x]
cambiar las listas para crear el producto por un diccionario []
agregar un codigo al diccionario de producto []
agregar una lista para almacenar los diccionarios de producto []
Modificar las funciones para que utilicen la nueva estructura de diccionario []
agregar las funciones faltantes:
    actualizar cantdad/precio []
    mostrar inventario completo []
    eliminar producto []
"""

def validarCodigo(codigo):
    contador_mayusculas=0
    for L in str(codigo):
        if L.isupper():
            contador_mayusculas+=1
        if L.isnumeric():
            contador_numeros+=1
    
    if contador_mayusculas<2:
        print("El codigo debe de tener al menos 2 mayusculas")
        return False
    elif contador_numeros==0:
        print("El codigo debe tener al menos 1 numero")
        return False
    elif len(codigo) <5:
        print("El codigo debe de tener al menos 5 caracteres")
        return False
    else:
        return True
    

def solicitarProducto():
    nombre=input("Ingrese el nombre del producto: ")
    while True:
        codigo=input("Ingrese el codigo para el producto: ")
        if validarCodigo(codigo)==True:
            print("Codigo correcto!.")
            break
        else:
            print("El codigo es incorrecto. Debe volver a ingresarlo")
    try:
        stock=int(input("Ingrese el stock del producto: "))
        precio=int(input("Ingrese el precio del producto: "))
            
        if stock<0 or precio <0:
                raise ValueError
                
        else:
            producto=[nombre,precio,stock]
            return producto

    except ValueError:
        print("Debe ingresar valores enteros positivos")

def guardarProducto(nombre,precio,stock,codigo):
    productoBuscado=buscarProducto(codigo)
    if productoBuscado !=None:
            print("Ese producto ya fue registrado")
            return False
    
    producto={"nombre": nombre,"precio": precio,"cantidad": stock,"codigo": codigo}
    lista_productos.append(producto)
    return True

    
def buscarProducto(nombre):
    for dictProducto in lista_productos:
        if codigo==dictProducto["codigo"]:
            return dictProducto
        
    return None

def mostrarProducto(codigo):
    productoBuscado=buscarProducto(codigo)
    if productoBuscado !=None:
        print("-"*60)
        print(f"Cod: {productoBuscado["codigo"]} \tNombre: {productoBuscado["nombre"]} \tPrecio: ${productoBuscado["precio"]} \tcantidad {productoBuscado["stock"]} ")
        

    else:
        print("No existe un producto con ese nombre")
    
    match opcion:

        case "1":
            nuevoProducto=solicitarProducto()
            if nuevoProducto!= None:
                guardarProducto(nuevoProducto[0],nuevoProducto[1],nuevoProducto[2])
        case "2":
            nombreProducto=input("Ingrese el nombre del producto a buscar: ")
            buscarProducto(nombreProducto)

