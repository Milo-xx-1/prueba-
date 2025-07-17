#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video], ...]
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'], }

#stock = {modelo: [precio, stock], ...]
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0], }


#opcion 1
def stock_marca(marca):
    if not marca:
        print("No existe ese modelo en nuestro stock")
    else:
        for marca, info in stock.items():
            print(f"marca: {marca} | stock: {stock}")
#opcion 2
def busqueda_precio(p_min, p_max):
    precio = float(input("Ingrese el precio del producto: "))
    encontrados = [p_min, p_max]
    for precio in stock.items():
        if precio in precio:
            encontrados.append(stock)
    if encontrados:
        print(f"Precio de productos {p_min, p_max}:{','.join(encontrados)}")
    else:
        print("No hay notebooks en ese rango de precios")
#opcion 3
def actualizar_precio(modelo, precio):
    try:
        modelo = input("Ingrese el precio del modelo a actualizar: ").upper()
        if modelo in productos:
            print("No tenemos este modelo en nuestro stock")
            return
        Modelo = input("Ingrese la marca del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        productos[modelo] = {"Modelo": Modelo,"precio": precio}
        print("Precio actualizado del modelo")
        print("Desea actualizar otro precio (s/n)???: ")
    except ValueError:
        print("Error, porfavor ingrese valores validos porfavor")


def menu():
    while True:
        print("************Bienvenido al menu*****************")
        print("1.- Stock marca")
        print("2.- Búsqueda por precio")
        print("3.- Actualizar precio")
        print("4.- Salir")
        opcion = input("Seleccione una opcion del 1-4: ")
        if opcion == '1':
             stock_marca()
        elif opcion == '2':
            busqueda_precio()
        elif opcion == '3':
            actualizar_precio()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Debe seleccionar una opción válida")





menu()