ANormal = 78900
AVip = 240000
NombreP = ""
RutP = ""
filas = 7
columnas = 6
contador = 1
seleccionados = [[False] * columnas for m in range(filas)]

print("---------------------------")
print("Bienvenido a VuelosDuoc")
print("---------------------------")

while True:
    try:

        print("Elija una opcion porfavor")
        print("1. Ver asientos disponibles.")
        print("2. Comprar asiento.")
        print("3. Anular vuelo.")
        print("4. Salir.")
        OpMenu = int(input(""))
        if OpMenu == 1:
            print("""
                |   1    2    3                 4     5      6  |
                |   7    8    9                 10    11    12  |
                |   13   14   15                16    17    18  |
                |   19   20   21                22    23    24  |
                |   25   26   27                28    29    30  |
                |______________________ ________________________|
                |______________________ ________________________|
                |   31   32   33                34    35   36   |
                |   37   38   39                40    41   42   |
                """)
            op = int(input("Ingrese su asiento a tomar: "))
    except ValueError:
            print("No se ha podido leer su opción.")
    
