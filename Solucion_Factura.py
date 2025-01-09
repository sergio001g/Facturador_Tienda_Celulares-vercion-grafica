#Registro de Usuario
usuarios = {}
def registro_Usuario():
    print(" ")
    while True:
        usuario = input("Ingrese un nombre de usuario: ")
        if usuario in usuarios:
            print("El nombre de usuario ya está registrado. Intente con otro.")
        else:
            contraseña = input("Ingrese una contraseña: ")
            usuarios[usuario] = {"contraseña": contraseña, "factura": None}
            print("-" * 100)
            print(f"{"":<35}Usuario registrado con éxito.")
            print("-" * 100)
            break

#Inicio de sesion
def login():
    print(" ")
    while True:
        usuario = input("Ingrese su nombre de usuario: ")
        contraseña = input("Ingrese su contraseña: ")
        print("")

        if usuario in usuarios and usuarios[usuario]["contraseña"] == contraseña:
            print("-" * 100)
            print(f"{"":<40}Inicio de sesion exitoso")
            print("-" * 100)
            print(f"Bienvenido, {usuario}.\n")
            return usuario
        else:
            print("Usuario o contraseña incorrectos. Intente nuevamente.\n")

#Datos factura (Cliente) nombre, identificacion, telefono, domicilio, correo
def datos_Factura():
    print("\nIngrese los datos solicitados para los datos de la factura.")
    print("-" * 100)
    #Nombres
    while True:
        nombre = input("Ingrese su nombre y apellido: ")
        if nombre.strip():
            break 
        else:
            print("No puede dejar el campo vacío. Por favor, ingrese su nombre y apellido.")
    print("-" * 100)
    #Cedula o RUC
    while True:
        print("Desea ingresar:")
        print("1. Cedula")
        print("2. RUC")
        CoR = input("Cual es su opcion: ")
        #Cedula 
        if CoR == "1":
            while True:
                def calcular_digito_verificador(cedula):
                    coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]
                    resultados = []
                    # Paso 1: Multiplicar cada dígito por su coeficiente
                    for i in range(9):
                        multiplicacion = int(cedula[i]) * coeficientes[i]
                        # Si el resultado es mayor a 10, sumar los dígitos
                        if multiplicacion > 9:
                            multiplicacion = sum(map(int, str(multiplicacion)))
                        resultados.append(multiplicacion)
                    # Paso 2: Sumar los resultados
                    suma_total = sum(resultados)
                    # Paso 3: Calcular el residuo de la división sobre 10
                    residuo = suma_total % 10
                    # Si el residuo es diferente de 0, el dígito verificador será 10 menos el residuo
                    digito_verificador = 0 if residuo == 0 else 10 - residuo
                    return digito_verificador
                cedula = input("Ingrese el numero de cedula: ")
                verificador_calculado = calcular_digito_verificador(cedula)
                if verificador_calculado == int(cedula[-1]):
                    print("La cédula es válida.")
                    identificacion = cedula
                    break
                else:
                    print("La cédula no es válida.")
            break
        #RUC
        elif CoR == "2":
            while True:
                ruc = input("Ingrese el numero de RUC: ")
                if len(ruc) == 13 and ruc.endswith("001"):
                    print("El RUC es valido.")
                    identificacion = ruc
                    break
                else:
                    print("Numero de RUC no valido. Intente nuevamente.")
            break
    
    #Direccion
    print("-" * 100)
    direccion = input("Ingrese la direccion de domicilio: ")
    print("-" * 100)
    
    #Telefono
    while True:
        telefono = input("Ingrese el numero de telefono: ")
        if len(telefono) == 10:
            print("El numero de telefono es valido.")
            break
        else:
            print("El numero de telefono no es valido.")
    print("-" * 100)
     
    #Correo Electronico
    while True:
        correoElectronico = input("Ingrese el correo electronico: ")
        if "@" in correoElectronico and "." in correoElectronico.split("@")[-1]:
            print("El correo electrónico es válido.")
            break
        else:
            print("El correo electrónico no es válido.")
    print("=" * 100)
    print("Los datos ingresados para la factura son:\n")
    
    print("=" * 100)
    
    return {
        "nombre": nombre,
        "identificacion": identificacion,
        "telefono": telefono,
        "direccion": direccion,
        "correo": correoElectronico,
    }

#Datos factura (Consumidor Final)
def datos_ConsumidorFinal(datos_factura):
    if datos_factura is None:
        datos_factura = {}
    return {
        'nombre': datos_factura.get('nombre', 'Consumidor Final').upper(),
        'identificacion': datos_factura.get('identificacion', '9999999999'),
        'telefono': datos_factura.get('telefono', '0000000000'),
        'direccion': datos_factura.get('direccion', 'N/A').upper(),
        'correo': datos_factura.get('correo', 'N/A').upper()
    }

#Catalogo   
def catalogo():
    while True:
        print("\nProductos disponibles:")
        print("° iPhone 16 - $999.99") 
        print("° Samsung Galaxy S23 - $899.99")
        print("° Cargador Universal - $19.99")
        print("° Funda Protectora - $25.99")

        opcion = input("\nEscriba `Salir` para volver al inicio: ").strip().lower()
        if opcion == "salir":
            print("-" * 100)
            break
        else:
            print("Opcion no valida. Intentelo de nuevo")

#Menu de compra
def menu_productos():
    productos = {
        1: {"nombre": "iPhone 16", "precio": 999.99},
        2: {"nombre": "Samsung Galaxy S23", "precio": 899.99},
        3: {"nombre": "Cargador Universal", "precio": 019.99},
        4: {"nombre": "Funda Protectora", "precio": 025.99},
    }

    compra = []

    while True:
        print("\nProductos disponibles:")
        for key, value in productos.items():
            print(f"{key}. {value['nombre']} - ${value['precio']:.2f}")
        print("5. Finalizar compra")

        opcion = int(input("\nSeleccione el producto que desea comprar (1-5): "))
        if opcion == 5:
            break
        elif opcion in productos:
            cantidad = int(input(f"Ingrese la cantidad de {productos[opcion]['nombre']}: "))
            compra.append({"producto": productos[opcion]["nombre"], "precio": productos[opcion]["precio"], "cantidad": cantidad})
        else:
            print("Opción inválida. Intente nuevamente.")

    return compra

#Factura    
#Nota: Poner codigo del producto, y observacion
def Factura_corregida(datos_factura, compra):
    from datetime import datetime
    hoy = datetime.now()
    fecha = hoy.strftime("%d/%m/%Y")
    hora = hoy.strftime("%H:%M:%S")
    print("")
    print("=" * 61)
    print(" " * 20 + "FACTURA DE COMPRA")
    print("=" * 61)

    print("Tienda: Mika's Store")
    print("Dirección: Calle 123, Quito")
    print("Teléfono: +593 099 131 1404")
    print(f"Fecha de emision: {fecha}    Hora: {hora}")
    print("-" * 61)

    #Datos de la factura
    datosCliente_ConsumidorFinal = datos_ConsumidorFinal(datos_factura)
    print(f"Cliente: {datosCliente_ConsumidorFinal['nombre']} - {datosCliente_ConsumidorFinal   ['identificacion']}")
    print(f"Teléfono: {datosCliente_ConsumidorFinal['telefono']}")
    print(f"Dirección: {datosCliente_ConsumidorFinal['direccion']}")
    print(f"Correo: {datosCliente_ConsumidorFinal['correo']}")
    print("-" * 61)

    #Datos de la compra
    print(f"{'Cantidad':<10}{'Descripción':<22}{'Precio Unitario':<21}{'Total':<12}")
    print("-" * 61)
    
    subtotal = 0
    for item in compra:
        total_producto = item["precio"] * item["cantidad"]
        subtotal += total_producto
        print(f"{"":>3}{item['cantidad']:<7}{item['producto']:<25}${item['precio']:<17.2f}${total_producto:<9.2f}")

    print("-" * 61)

    impuestos = subtotal * 0.15
    total = subtotal + impuestos

    print(f"{'Subtotal':<35}${subtotal:.2f}")
    print(f"{'Impuestos (15%)':<35}${impuestos:.2f}")
    print(f"{'Total':<35}${total:.2f}")
    print("=" * 61)

    print(" " * 20 + "¡Gracias por su compra!\n")

#Control de inicio de sesion, compra y generacion de factura
def menu_login_registroDatos():
    sesion_iniciada = login()
    if sesion_iniciada:
        while True:
            print("-" * 100)
            print("Nota: Si la factura quiere con consumidor final. Puede ir directamente a la opcion ´3´ ")
            print("-" * 100)
            print("1. Registrar datos de factura")
            print("2. Ver datos de factura")
            print("3. Ver catalogo y comprar")
            print("4. Salir")
            Op = input("Seleccione una opción: ")
            
            if Op == "1":
                factura = datos_Factura()
                usuarios[sesion_iniciada]["factura"] = factura
                print("Datos de factura registrados con éxito.")
            elif Op == "2":
                factura = usuarios[sesion_iniciada].get("factura")
                if factura:
                    print("=" * 100)
                    print("Datos de la factura:\n")
                    for clave, valor in factura.items():
                        print(f"{clave.capitalize()}: {valor.upper()}")
                    print("=" * 100)
                else:
                    print("-" * 100)
                    print("No se han registrado datos de factura.")
                    print("-" * 100)
            elif Op == "3":
                carrito_compra = menu_productos()
                imFac = input("¿Desea imprimir la factura? (Si/No): ").strip().lower()
                if imFac == "si":
                    factura = usuarios[sesion_iniciada].get("factura", None)
                    Factura_corregida(factura, carrito_compra)
                else:
                    print(" " * 20 + "¡Gracias por su compra!\n")
            elif Op == "4":
                print("-" * 100)
                break

