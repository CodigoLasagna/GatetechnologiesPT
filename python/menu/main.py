from os import system, name
import time

class Empleado:
    def __init__(self, ID, Nombre, ApeP, ApeM, fechNac):
        self.ID = ID
        self.Nombre = Nombre
        self.ApeP = ApeP
        self.ApeM = ApeM
        self.fechNac = fechNac

def main():
    empleados =  []
    empleados.append(Empleado(16, "Jaime", "Flores", "Hernandez", "16/04/2022"))
    menu()

def menu():
    opt = ""
    while(opt != '0'):
        dibujarMenu()
        opt = input(">")
        limpiarPantalla()
        if (opt == '1'):
            registrarEmpleado()
        if (opt == '2'):
            pass
        if (opt == '3'):
            pass
        if (opt == '4'):
            pass
        if (opt == '0'):
            pass

def dibujarMenu():
    limpiarPantalla()
    print("Registrar empleado...............................[1]")
    print("Obtener la edad del empleado por ID..............[2]")
    print("Obtener lista de empleados por orden alfabético..[3]")
    print("Obtener lista de empleados por edad..............[4]")
    print("Salir............................................[0]")

def registrarEmpleado():
    ID = 0; Nombre = ApeP = ApeM = fechaNac = ""
    ans = ""
    
    while(not(ans.isnumeric())):
        limpiarPantalla()
        ans = input("Introduzca un ID numericamente valido.\n>")
        # Comprobar si el ID existe
        if (not(ans.isnumeric())):
            print("ID no valido.")
            time.sleep(0.75)
    ID = int(ans)
    ans = input("Introduzca el nombre\n>")


def limpiarPantalla():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


if __name__ == "__main__":
    main()

