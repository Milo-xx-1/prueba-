Usuario = {}
Contraseña = {}
Sexo = {}

# Función para registrar el Usuario
def registrar_Usuario():
    while True:
        patente = input("Ingrese el usuario: ").upper()
        if validar_Contraseña(Contraseña):
            if Contraseña in Usuario:
                print("El usuario ya está registrado.")
            else:
                break
    Usuario = input("Ingrese su Usuario: ")

    while True:
        sexo = input("Ingrese el sexo del dueño (M/F): ").upper()
        if validar_sexo(sexo):
            break

    Usuario[Contraseña] = {'Nombre': Usuario,
                           'Sexo': sexo,
                           'Contraseña': Contraseña }
    print("Usuario registrado correctamente.\n")

# Validaciones
def validar_Contraseña(Contraseña):
    if len(Contraseña) != 8:
        print("La contraseña debe tener un minimo de 8 caracteres.")
        return False
    return True

def validar_sexo(sexo):
    if sexo.upper() not in ['M', 'F']:
        print("El sexo debe ser 'M' o 'F'.")
        return False
    return True

# Función para eliminar Usuario
def eliminar_Usuario():
    patente = input("Ingrese la contraseña del Usuaio a eliminar: ").upper()
    if Contraseña in Usuario:
        del Usuario[Contraseña]
        print("Usuario eliminado correctamente.\n")
    else:
        print("Este Usuario no está registrado.\n")

# Función para Buscar Usuario
def buscar_Usuario():
    if not Usuario:
        print("No hay Usuaios registrados.\n")
    else:
        for Usuario in Contraseña():
            print(f"Usuario: {Usuario}")
            print(f"Contraseña: {Contraseña}")
            print("-" * 30)



# Menú principal
def menu():
    while True:
        print("\n--- Sistema de Registro de Vehículos ---")
        print("1. Registrar Usuario")
        print("2. Buscar Usuario")
        print("3. Eliminar Usuario")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_Usuario()
        elif opcion == '2':
            buscar_Usuario()
        elif opcion == '3':
            eliminar_Usuario()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.\n")

# Ejecutar menú
menu()