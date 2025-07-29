"""PARCIAL PRIMRERA PARTE"""
empleados = {}
opcion = 0

while opcion!=4:
    print("+++ MENU+++")
    print("1. Registrar emplados")
    print("2. Mostar empleados")
    print("3. Buscar empleados")
    print("4. Salir")
    try:
        opcion= int(input("Ingrese su opcion: "))
    except ValueError:
        print("ERROR, ingrse un dato valido...")

    match opcion:
        case 1:
            cantidad = int(input("¿Cuantos empleados desea registrar?: "))
            for i in range (cantidad):
