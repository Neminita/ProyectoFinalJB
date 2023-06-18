print("---------------------------")
print("Bienvenido a VuelosDuoc")
print("---------------------------")
filas = 6
columnas = 7

asientos = [[(i * columnas + j + 1) for j in range(columnas)] for i in range(filas)]


def Masientos():
    for fila in asientos:
        print("|", end="")
        for asiento in fila:
            if asiento == "x":
                print("   x", end="")
            else:
                print(f"{asiento:4}", end="")
        print("|")


while True:
    try:
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
        elif OpMenu == 4:
            print("Gracias por Elegirnos")
            break
    except ValueError:
        print("INGRESE OPCIÓN VALIDA")
