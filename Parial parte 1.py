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
                print(f"Emplados {i+1}")
                codigo = input("Ingrese el codigo de empleado: ")
                while True:
                    if codigo in empleados:
                        print("Este emplado ya ha sido registrado...")
                    else:
                        empleados[codigo]= {}
                        break

                empleados[codigo]["nombre"]= input("Ingrese el nombre del empleado: ")
                empleados[codigo]["departamento"] = input("Ingrese el departamanto del empleado: ")
                empleados[codigo]["antiguedad"] =  input("Ingerse los años de antiguedad del empleado en la empresa: ")
                empleados[codigo]["contacto"]= {
                    "telefono": input("Ingrese el telefono del empleado: "),
                    "correo": input("Ingrese el correo del empleado")
                  }

                empleados[codigo]["evaluacion"] = {}
                codigo_evalucion = input("Ingrese el codigo del proyecto: ")
                empleados[codigo]["evaluacion"][codigo_evalucion] = {
                    "puntualidad": int(input("Ingrese la puntualidad del usuario: ")),
                    "equipo": int(input("Ingrase el nivel de trabajo en equipo del empleado: ")),
                    "observaciones": int(input("Ingrese observaciones del empleado: ")),
                }

        case 2:
            print("\nLista de Empleados registrados: ")
            for codigo, data in empleados.items():
                print(f"Codigo: {codigo}")
                print(f"Nombre del empleado: {data['nombre']}")
                print(f"Departamento: {data['departamento']}")
                print(f"Antiguedad en la empresa: {data['antiguedad']}")
                print("Contactos:")
                print(f"Correo: {empleados[codigo]['contacto']['correo']}")
                print(f"Telefono: {empleados[codigo]['contacto']['telefono']}")
                print("Evalucion: ")
                for codigo_evalucion in empleados[codigo]["evaluacion"]:
                    print(f"\tCodigo de la evaluacion: {codigo_evalucion}")
                    print(f"\tPuntualidad: {empleados[codigo]['evalucion'][codigo_evalucion]['puntualidad']} ")
                    print(
                        f"\tDesempeño en equipo: {empleados[codigo]['evalucion'][codigo_evalucion]['desempeño_equipo']}")


