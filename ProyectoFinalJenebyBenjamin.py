print("Probando sincronización")
print("Testeo 2.0")
print("Testeo rama benja")


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
        print("4. Cambiar Datos.")
        print("5. Salir")
        OpMenu = int(input(""))

        if OpMenu == 1:
            def mostrar_lista():
                contador = 1  # Variable para rastrear el número actual a imprimir
                for i in range(filas):
                    for j in range(columnas):
                        if seleccionados[i][j]:
                            print('x', end='\t')  # Imprimir 'x' si el número está seleccionado
                        else:
                            print(contador, end='\t')  # Imprimir el número actual si no está seleccionado
                        contador += 1  # Incrementar el contador para el siguiente número
                    print()  # Imprimir una nueva línea al final de cada fila

            def marcar_numero(numero):
                if numero < 1 or numero > filas * columnas:
                    print("Número inválido. Inténtalo nuevamente.")
                    return
                fila = (numero - 1) // columnas  # Calcular la fila correspondiente al número seleccionado
                columna = (numero - 1) % columnas  # Calcular la columna correspondiente al número seleccionado
                seleccionados[fila][columna] = True  # Marcar el número como seleccionado

            while True:
                mostrar_lista()  # Mostrar la lista actual
                NumeroSeleccionado = int(input("Elija el asiento deseado: "))

                if NumeroSeleccionado >= 1 and NumeroSeleccionado <= 30:
                    print("Este asiento tiene un valor de: $",ANormal)
                    print("Desea ese u otro?")
                    print("1. SI")
                    print("2. NO")
                    SeleccionA = int(input(""))

                if NumeroSeleccionado <= 31 and NumeroSeleccionado >= 42:
                    print("Este asiento tiene un valor de: $",AVip)    
                    print("Desea ese u otro?")
                    print("1. SI")
                    print("2. NO")
                    SeleccionA = int(input(""))

                    if SeleccionA == 1:
                        break

                    if SeleccionA == 2:
                        NumeroSeleccionado == 0

        if OpMenu == 2:
            while True:
                try:
                    if NombreP == "":
                        print("Digite su nombre")
                        NombreP = input("")

                        if NombreP == "":
                            print("Digite un nombre porfavor")
                            continue

                        
                    if RutP == "":
                        print("Digite su rut")
                        RutP = input("")

                        if RutP == "":
                            print("Digite un rut porfavor")
                            continue
                        
                    print("Digite su numero de telefono, sin codigo de pais")
                    NumeroP = int(input(""))

                    print("Elija su banco")
                    print("1. Banco DUOC")
                    print("2. Banco Estado")
                    print("3. Banco de Chile")
                    print("4. Otro")
                    BancoP = int(input(""))

                    if BancoP <= 0 or BancoP >= 5:
                        print("Digite un numero valido")

                    
                
                except ValueError:
                        print("Digite algo valido")
                        continue            

        if OpMenu == 3:
            NumeroSeleccionado == 0
            print("Vuelo anulado")
            VueloT = 0

        if OpMenu == 4:
            print("Cerrando sistema...")
            break

        if OpMenu == 5:
            print("Digite su rut")
            RutModificar = input("")
            print("Digite el asiento comprado")
            AsientoModificar = int(input(""))

            if RutModificar == RutP and AsientoModificar == NumeroSeleccionado:
                print("Que desea modificar?")
                print("1. Nombre Pasajero")
                print("2. Telefono Pasajero")
                OpModificar = int(input(""))
                
                if OpModificar == 1:
                    print("Digite el nombre deseado")
                    NombreP == input("")

                if OpModificar == 2:
                    print("Digite su nuevo numero de telefono")
                    NumeroP == input("")    

            else:
                print("Datos invalidos dentro de la base de datos")
                
        if OpMenu <= 0 or OpMenu >= 6:
            print("Digite una opcion valida")

        print("Su total es de:")        

    except ValueError:
        print("Digite una opcion valida")
        continue

