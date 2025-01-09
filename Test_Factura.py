import Solucion_Factura

print("*-" * 50)
print(f"\n{"":<25}✨¡Bienvenido a tu mundo de tecnología y conexión!✨ \n{"":<45}Mika's Store\n")
print(f"{"":<22}📱´Conéctate con el futuro, elige tu próximo celular hoy´📱\n")
print(f"En Mika, encontrarás los mejores celulares, accesorios de última generación y un servicio pensado \nespecialmente para ti. \n{"":<18}¡Explora, elige y lleva contigo la tecnología que conecta tu mundo!")
print("-" * 100)
print("-Elija una de las siguientes opciones.")
print("[Nota: Para realizar una compra debe registrarse e iniciar sesion]")
print("-" * 100)
while True:
        print(f"{"":<44}Menú Principal")
        print("-" * 100)
        print("1. Ver catalogo")
        print("2. Registrar usuario")
        print("3. Iniciar sesión")
        print("4. Salir\n")
        opcion = input("Seleccione una opción (1-4): ")
    
        if opcion == "1":
            Solucion_Factura.catalogo()
        elif opcion == "2":
            Solucion_Factura.registro_Usuario()
        elif opcion == "3":
            Solucion_Factura.menu_login_registroDatos()
        elif opcion == "4":
            print("-" * 100)
            print(f"{"":<25}Gracias por visitar Mika's Store. ¡Vuelva pronto!")
            print("-" * 100)
            break
        else:
            print("Opción no válida. Intente nuevamente.\n")

