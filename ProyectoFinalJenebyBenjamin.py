print("---------------------------")
print("Bienvenido a VuelosDuoc")
print("---------------------------")
filas = 6
columnas = 7
ANormal = 78900
AVip = 240000

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

        # Definicion de Funcion para datos de usuario o pasajero


def DatosUsuario():
    print("Ingrese sus datos correspondientes. ")
    RutUs = int(input("Ingrese su rut sin guíon ni puntos: "))
    if RutUs != int:
        print("Formato inválido")
    NomUs = str(input("Ingrese su nombre completo: "))
    if NomUs != str:
        print("Formato inválido.")
    TelefUs = int(input("Ingrese su teléfono de contacto: "))
    if TelefUs != int:
        print("Formato inválido.")
    BancoUs = str(input("Ingrese el nombre de su banco: "))
    if BancoUs != str:
        print("Formato inválido.")

    # Primera interfaz de menú.


while True:
    try:
        cont = 0
        print("Elija una opcion porfavor")
        print("1. Ver asientos disponibles.")
        print("2. Comprar asiento.")
        print("3. Anular vuelo.")
        print("4. Salir.")
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
                print(f"El valor de éste pasaje es: {ANormal}")
                print(
                    """
            ¿Quisiera confirmar su compra?
            1.Si
            2.No
            """
                )
                confus = int(input())
                if confus == 1:
                    DatosUsuario()
                else:
                    cont = 0
            elif eleccion > 30 and eleccion <= 42:
                print(f"El valor de éste asiento VIP es: {AVip}")
                print(
                    """
            ¿Quisiera confirmar su compra?
            1.Si
            2.No
            """
                )
                confus = int(input())
                if confus == 1:
                    DatosUsuario()
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
    except ValueError:
        print("INGRESE OPCIÓN VALIDA")
