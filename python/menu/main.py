from os import system, name
import time
import operator
from datetime import date
import validarFecha

#se define la clase
class Empleado:
    def __init__(self, ID, Nombre, ApeP, ApeM, FechNac):
        self.ID = ID
        self.Nombre = Nombre
        self.ApeP = ApeP
        self.ApeM = ApeM
        self.FechNac = FechNac

#inicia la aplicación
def main():
    menu()

#menu principal
def menu():
    opt = ""                # variable para determinar la opción escogida
    contadorID = 0          # variable para determinar el ID automatico de los empleados
    empleados =  []         # lista para almacenar los empleados
    while(opt != '0'):      # minetras que no se escoja la opción 0 se puede escoger cualquier otra opción
        dibujarMenu()       # Se llama a la función para dibujar la interfaz en terminal
        opt = input("Teclee una opción y presione enter\n>")    # Se dibuja un señalamiento para introducir una opción
        limpiarPantalla()   # se limpia la consola
        if (opt == '1'):    # si se escoge la primer opción se llama a la función para registrar empleados
            contadorID = registrarEmpleado(empleados, contadorID) # En caso de registrar el empleado correctamente se incrementa el contador de ID
        if (contadorID > 0):    # mientras haya registros las siguientes opciones funcionan
            if (opt == '2'):    # si se escoge la opcion 2 se entra a la sección para obtener la edad de un empleado por ID
                obtenerEdadPorID(empleados, contadorID)
            if (opt == '3'):    # si se escoge la opcion 3 se despliegan a los empleados por apellido y orden alfabético
                ordenAlfabetico(empleados)
            if (opt == '4'):    # si se escoge la opción 4 se despliegan a los empleados por edad
                ordenEdad(empleados)
        else:
            if ( opt != '0'):
                print("Aun no se han creado registros.")
                time.sleep(0.75)

# funcion para dibujar el menu
def dibujarMenu():
    limpiarPantalla()   # se limpia la pantalla para luego dibujar el menu
    print("Registrar empleado...............................[1]")
    print("Obtener la edad del empleado por ID..............[2]")
    print("Obtener lista de empleados por orden alfabético..[3]")
    print("Obtener lista de empleados por edad..............[4]")
    print("Salir............................................[0]")

# funcion para registrar los empleados
def registrarEmpleado(empleados, contadorID):
    Nombre = ApeP = ApeM = fechNac = ""     # se inician las variables básicas
    ans = ""                                # variable para recibir las entradas del formulario
    valid = False                           # variable de soporte para verificar las entradas

    while(valid == False):                      # si el nombre o apellidos cumplen con las condiciones básicas de un nombre se aceptan y luego se
        ans = input("Introduzca el nombre\n>")  # altera para que corresponda a un formato estandar 
        valid = validName(ans, valid)
    Nombre = ans.lower().title().strip()
    valid = False   # para pasar al siguiente paso en cada parte del formulario se resetea la función de validación

    while(valid == False):
        ans = input("Introduzca el apellido paterno\n>")
        valid = validName(ans, valid)
    ApeP = ans.lower().title().strip()
    valid = False

    while(valid == False):
        ans = input("Introduzca el apellido materno\n>")
        valid = validName(ans, valid)
    ApeM = ans.lower().title().strip()
    valid = False

    while(valid == False):          # Para comprobar la fecha se utiliza una funcion previamente creata en esta prueba técnica
        ans = input("Introduzca una fecha con el siguiente Formato dd/MM/yyyy\n>")
        valid = validarFecha.validar(ans)
        if (valid == True):
            if (calcEdad(ans) < 18):    # si el solicitante tiene menos de 18 años no se acepta
                valid = False
                print("Menor de edad, no puede trabajar...")
                time.sleep(0.75)
    fechNac = ans
    valid = False

    while(valid == False):  # aqui se decide si se registra el empleado o no (en caso de cometer un error se puede negar)
        limpiarPantalla()
        print("ID: "+str(contadorID))
        print("Nombre: "+Nombre)
        print("Apellido paterno: "+ApeP)
        print("Apellido materno: "+ApeM)
        print("Fecha de nacimiento: "+fechNac)
        ans = input("\n¿Desea agregar este empleado? [S]i [N]o\n>")
        ans = ans.upper()       # la respuesta solo se valida si es una de las dos opciones, posteriormente se ajusta
        if (ans == 'S'):        # para funcionar con mayusculas y minusculas
            day = int(fechNac[0:2])   # se disecciona la fecha de nacimiento en dia, mes y año
            month = int(fechNac[3:5])
            year = int(fechNac[6:10])
            empleados.append(Empleado(contadorID, Nombre, ApeP, ApeM, date(year, month, day))) # se registra al empleado en caso de ser aceptado
            valid = True
            print("Se ha agregado el empleado nuevo")
            time.sleep(0.75)
            return contadorID + 1   # se retorna el contador de ID mas uno
        elif (ans == 'N'):
            valid = True
            print("Saliendo...")
            return contadorID       # en caso de rechazarse se retorna el contador como esta
            time.sleep(0.75)
        else:
            print("Respuesta no valida")

# funcion para validar el nombre
def validName(nombre, valid):
    cont = 0    # variable para contar los caracteres alfanumericos
    if (all(x.isalpha() or x.isspace() for x in nombre) and len(nombre) >= 2):  # se toma en cuenta que contenga solo espacios
        for x in nombre:                                                        # y caracteres alfanumericos ademas de un tamaño mayor a dos
            if (x.isalpha() == True):                                           # se cuentan los caracteres alfanumericos para comprobar que minimo sean 2
                cont += 1

    if (cont >= 2):     # si se cumplen todas las condiciones se valida
        valid = True
    else:
        print("Un nombre necesita al menos dos caracteres alfanumericos, y no numeros ni estar vacio")

    return valid

# funcion para obtener la edad
def obtenerEdadPorID(empleados, contadorID):
    ans = ""            # Variable para recibir las respuestas
    ID = -1             # variable para almacenar el ID pedido
    edad = 0            # variable para almacenar la edad
    valid = False       # variable auxiliar para validar en la funcion
    while(valid == False):  # mientras se reciban datos invalidos se repite la funcion
        limpiarPantalla()   # se limpia la pantalla
        ans = input("Introduzca el ID del empleado\n>") #se pide el ID
        if (ans.isnumeric() == True):   # si el ID es validamente numerico se acepta
            ID = int(ans)
            if (ID < contadorID):       # si el ID entra en el rango de IDs existentes se valida
                valid = True
            else:
                print("El ID no existe, fuera de rango.")
                time.sleep(0.75)
        else:
            print("No es un ID valido")
            time.sleep(0.75)
    edad = calcEdadProc(empleados[ID].FechNac)  # se llama a la funcion para calcular la edad
    print(empleados[ID].Nombre+" tiene "+str(edad)+" años")  # se imprime la edad calculada
    input("\nPresione cualquier tecla para continuar...")

# Funcion para calcular la edad
def calcEdad(fecha):
    presente = date.today() # se pide la fecha actual

    day = int(fecha[0:2])   # se disecciona la fecha de nacimiento en dia, mes y año
    month = int(fecha[3:5])
    year = int(fecha[6:10])
    FechNac = date(year, month, day)    # se convierte en una fecha para trabajar

    edad = presente.year - FechNac.year - ((presente.month, presente.day) < (FechNac.month, FechNac.day)) # se calcula la edad
    return edad # se retorna la edad

# Funcion para calcular la edad una vez se ha procesado en formato
def calcEdadProc(fecha):
    presente = date.today() # se pide la fecha actual
    edad = presente.year - fecha.year - ((presente.month, presente.day) < (fecha.month, fecha.day)) # se calcula la edad
    return edad # se retorna la edad

# Funcion para desplegar los empleados en orden alfabetico por el apellido
def ordenAlfabetico(empleados): 
    listaOrdenada = sorted(empleados, key = operator.attrgetter('ApeP'))    # se ordena una lista auxiliar para no alterar la original en base al apellido paterno
    for x in listaOrdenada:     # se obtiene cada empleado dentro de la lista auxiliar
        print("[ID:"+str(x.ID)+"] [Nombre: "+x.Nombre+" "+x.ApeP+" "+x.ApeM+"] [Fecha de Nac: "+str(x.FechNac.strftime("%d/%m/%Y"))+"] [Edad: "+str(calcEdadProc(x.FechNac))+"]") # se despliegan de forma ordenada
    input("\nPresione cualquier tecla para continuar...")

# Funcion para desplegar los empleados en orden por cumpleaños
def ordenEdad(empleados):
    listaOrdenada = sorted(empleados, key = operator.attrgetter('FechNac')) # se ordena una lista auxiliar en base a la fecha de nacimiento
    for x in listaOrdenada: # se obtiene cada empleado de la lista auxiliar
        print("[ID:"+str(x.ID)+"] [Nombre: "+x.Nombre+" "+x.ApeP+" "+x.ApeM+"] [Fecha de Nac: "+str(x.FechNac.strftime("%d/%m/%Y"))+"] [Edad: "+str(calcEdadProc(x.FechNac))+"]") # se despliega de forma ordenada
    input("\nPresione cualquier tecla para continuar...")

# Funcion para limpiar la consola
def limpiarPantalla():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


if __name__ == "__main__":
    main()

