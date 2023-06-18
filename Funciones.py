print("---------------------------")
print("Bienvenido a VuelosDuoc")
print("---------------------------")
filas = 6
columnas = 7
ANormal = 78900
AVip = 240000
descuento = 0
descuento2 = 0

asientos = [[(i * columnas + j + 1) for j in range(columnas)] for i in range(filas)]


# Definicion de Funcion para crear el menú de asientos y sus arreglos
def Masientos():
    for fila in asientos:
        print("|", end="")
        for asiento in fila:
            if asiento == "x":
                print("   x", end="")
            else:
                print(f"{asiento:4}", end="")
        print("|")


# Datos de usuario para ingresar en normal.


def UsuarioNormal():
    print("Ingrese sus datos correspondientes. ")
    RutUs = str(input("Ingrese su rut sin guíon ni puntos: "))
    NomUs = str(input("Ingrese su nombre completo: "))
    TelefUs = int(input("Ingrese su teléfono de contacto: "))
    BancoUs = str(input("Ingrese el nombre de su banco: "))
    if (
        BancoUs == "BancoDuoc"
        or "Bancoduoc"
        or "bancoDuoc"
        or "BancoDuoc"
        or "BANCODUOC"
        or "bancoduoc"
    ):
        descuento = (ANormal) * 0.15
        print("El valor NORMAL de éste pasaje es:", (ANormal - descuento))
    else:
        descuento = 0
        print("El valor de éste pasaje es:", (ANormal))


# Datos de usuario para ingresar en Vip.
def UsuarioVip():
    print("Ingrese sus datos correspondientes. ")
    RutUs = int(input("Ingrese su rut sin guíon ni puntos: "))
    NomUs = str(input("Ingrese su nombre completo: "))
    TelefUs = int(input("Ingrese su teléfono de contacto: "))
    BancoUs = str(input("Ingrese el nombre de su banco: "))

    if (
        BancoUs == "BancoDuoc"
        or "Bancoduoc"
        or "bancoDuoc"
        or "BancoDuoc"
        or "BANCODUOC"
        or "bancoduoc"
    ):
        descuento = (AVip) * 0.15
        print("El valor VIP de éste pasaje es:", (AVip - descuento))
    else:
        descuento = 0
        print("El valor de éste pasaje es:", (ANormal))
    # Primera interfaz de menú.


def menu():
    while True:
        try:
            cont = 0
            print("Elija una opcion porfavor")
            print("1. Ver asientos disponibles.")
            print("2. Comprar asiento.")
            print("3. Anular vuelo.")
            print("4. Modificar cambios.")
            print("5. Salir.")
            OpMenu = int(input())
            if OpMenu == 1:
                Masientos()
            elif OpMenu == 2:
                Masientos()
                eleccion = int(input("Seleccione un asiento: "))
                if eleccion in [asiento for fila in asientos for asiento in fila]:
                    for i, fila in enumerate(asientos):
                        for j, asiento in enumerate(fila):
                            if asiento == eleccion:
                                asientos[i][j] = "   X"
                                break
                if eleccion >= 1 and eleccion <= 30:
                    print(
                        """
                ¿Quisiera confirmar su compra?
                1.Si
                2.No
                """
                    )
                    confus = int(input())
                    if confus == 1:
                        UsuarioNormal()

                    else:
                        cont = 0
                elif eleccion > 30 and eleccion <= 42:
                    print(
                        """
                ¿Quisiera confirmar su compra?
                1.Si
                2.No
                """
                    )
                    confus = int(input())
                    if confus == 1:
                        UsuarioVip()
                    else:
                        cont = 0
                else:
                    print("El valor no se ha encontrado.")
            elif OpMenu == 3:
                print(
                    """
                ¿Quisiera Anular envío?
                1.Si
                2.No
                """
                )
                anulacion = int(input())
                if anulacion == 1:
                    print("Su anulación ha sido exitosa!")
                else:
                    print("Se ha cancelado su anulación!")
            elif OpMenu == 4:
                print("Modificación de datos. ")
                nomus = int(input("Porfavor ingrese su nombre: "))
                eleccion = int(input("Porfavor ingrese su asiento: "))
                print("Bienvenido de nuevo!")

            elif OpMenu == 5:
                print("Gracias por utilizar el programa.")
                break

        except ValueError:
            print("INGRESE OPCIÓN VALIDA")
