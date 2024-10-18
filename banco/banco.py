#Programa para un banco
#solicitud para el programa
# Menu de opciones:
#   agregar Clientes
#   listar Clientes
#   Borrar Clientes
#   Editar Clientes
# Consola solicite los datos del cliente: Nombre, Apellido, Edad, Telefono y saldo.
# Que cada dato lo agregue a una lista: Nombres, Apellidos, edades y telefonos.
# Que tenga otra opcion para listar los clientes con datos y saldo.


nombres = []
apellidos = []
edades = []
telefonos = []
saldos = []
global opcion
opcion = 100
clientes = []
cliente = {}


def editar():
    print("ingrese el nombre del cliente a editar")
    nombre = input()
    for i in range(len(nombres)):
        if nombres[i] == nombre:
            nombres.remove(nombre)
            apellidos.remove(apellidos[i])
            edades.remove(edades[i])
            telefonos.remove(telefonos[i])
            saldos.remove(saldos[i])

def borrar():
    print("ingrese el nombre a borrar")
    nombre = input()
    for i in range(len(nombres)):
        if nombres[i] == nombre:
            nombres.remove(nombre)
            apellidos.remove(apellidos[i])
            edades.remove(edades[i])
            telefonos.remove(telefonos[i])
            saldos.remove(saldos[i])

def banco():
    print("Bienvenido al banco")
    print("Que actividad desea realizar")
    print("1. Agregar cliente")
    print("2. Listar cliente")
    print("3. Borrar cliente")
    print("4. Editar cliente")
    opcion = int(input("Digita la actividad a realizar"))
    if opcion == 1:
        print("Agregar cliente")
        print("Ingrese su nombre")
        nombres = input()
        cliente["nombres"]=nombres
        print("Ingrese sus apellidos")
        apellidos = input()
        cliente["apellidos"]= apellidos
        print("Ingrese su edad")
        edad = input()
        cliente["edades"]=edad
        print("Ingrese su numero telefonico")
        telefono = int(input())
        cliente["telefonos"]=telefono
        print("Ingrese su")
        saldo = int(input())
        cliente["saldo"]=saldo
        clientes.add[cliente]
    elif opcion == 2:
        print("Listar cliente")
        for i in range(len(nombres)):
            print(f"Cliente: {nombres[i]}, {apellidos[i]} Edad: {edades[i]}, Numero telefonico: {telefonos[i]}, Saldo: {saldos[i]} ")
banco()
