from os import system, name
import operator
from datetime import date
import validarFecha

# interfaz
import PySimpleGUI as sg

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
    contadorID = 0          # variable para determinar el ID automatico de los empleados
    empleados =  []         # lista para almacenar los empleados
    valid = False
    edad = 0
    noPop = True

    menuPrincipal = defineMenuPrinc()
    menuRegistro = defineMenuReg()
    menuEdadPorID = defineMenuEdadPorID()
    menuOrdPorAP = defineMenuOrdApe()
    menuOrdPorEdad = defineMenuOrdEdad()
    
    layout = [[
        sg.Column(menuPrincipal, key='-COL1-', element_justification='c', background_color="#1A1A1A"),
        sg.Column(menuRegistro, visible=False, key='-COL2-', background_color="#1A1A1A"),
        sg.Column(menuEdadPorID, visible=False, key='-COL3-', element_justification='c', background_color="#1A1A1A"),
        sg.Column(menuOrdPorAP, visible=False, key='-COL4-', element_justification='c', background_color="#1A1A1A"),
        sg.Column(menuOrdPorEdad, visible=False, key='-COL5-', element_justification='c', background_color="#1A1A1A")
        ]]
    window = sg.Window("Menu de empleados", layout, size=(500, 500), margins=(16, 50), element_justification='c', background_color="#1A1A1A")
    layout = 1
    
    while True:
        event, values = window.read()

        if event == "R1" or event == "R2" or event == "R3" or event == "R4":
            window[f'-COL{layout}-'].update(visible=False)
            layout = 1
            window[f'-COL{layout}-'].update(visible=True)
            cleanReg(window)
            noPop = False

        if event == "Salir" or event == sg.WIN_CLOSED:
            noPop = False
            break

        if event == "Registrar":
            noPop = False
            valid = registrarEmpleado(contadorID, values.get("Name"), values.get("AP"), values.get("AM"), values.get("FN"), valid)
            if (valid == True):
                day = int(values.get("FN")[0:2])   # se disecciona la fecha de nacimiento en dia, mes y año
                month = int(values.get("FN")[3:5])
                year = int(values.get("FN")[6:10])
                empleados.append(Empleado(contadorID, procNom(values.get("Name")), procNom(values.get("AP")), procNom(values.get("AM")), date(year, month, day))) 
                sg.Popup("Se ha registrado el empleado con el ID ["+str(contadorID)+"]", keep_on_top=True, background_color="#1A1A1A")
                cleanReg(window)
                window[f'-COL{layout}-'].update(visible=False)
                layout = 1
                window[f'-COL{layout}-'].update(visible=True)
                valid = False
                contadorID += 1

        if event == "Buscar":
            edad = obtenerEdadPorID(empleados, contadorID, values.get("BPID"))
            if (edad != 0):
                window["contEdad"].update(empleados[int(values.get("BPID"))].Nombre+" tiene "+str(edad)+" años.")


        if (layout == 1):
            window[f'-COL{layout}-'].update(visible=False)
            layout = seleccionarMenu(window, contadorID, noPop, event, empleados)
            window[f'-COL{layout}-'].update(visible=True)
            noPop = True

    window.close()

def seleccionarMenu(window, contadorID, noPop, event, empleados):
    layout = 1
    if event == "opt1":
        noPop = False
        layout = 2

    if contadorID > 0:
        if event == "opt2":
            layout = 3

        if event == "opt3":
            layout = 4
            for x in ordenAlfabetico(empleados):     # se obtiene cada empleado dentro de la lista auxiliar
                window["ordAlf"].update(window["ordAlf"].get()+"[ID:"+str(x.ID)+"] ["+x.Nombre+" "+x.ApeP+" "+x.ApeM+"] ["+str(x.FechNac.strftime("%d/%m/%Y"))+"] [Edad: "+str(calcEdadProc(x.FechNac))+"]\n") 

        if event == "opt4":
            layout = 5
            for x in ordenEdad(empleados):     # se obtiene cada empleado dentro de la lista auxiliar
                window["ordEdad"].update(window["ordEdad"].get()+"[ID:"+str(x.ID)+"] ["+x.Nombre+" "+x.ApeP+" "+x.ApeM+"] ["+str(x.FechNac.strftime("%d/%m/%Y"))+"] [Edad: "+str(calcEdadProc(x.FechNac))+"]\n") 
    else:
        if (noPop == True):
            sg.Popup("Aun no se han creado registros", keep_on_top=True, background_color="#1A1A1A")
    return layout

def cleanReg(window):
    window["Name"].update("")
    window["AP"].update("")
    window["AM"].update("")
    window["FN"].update("")
    window["contEdad"].update("")
    window["BPID"].update("")
    window["ordAlf"].update("")
    window["ordEdad"].update("")

def defineMenuPrinc():
    menuPrincipal = [
            [sg.Button(button_text="Registrar empleado.", key="opt1")],
            [sg.Button("Obtener edad de empleado por ID.", key="opt2")],
            [sg.Button("Desplegar lista de empleados en orden alfabetico.", key="opt3")],
            [sg.Button("Desplegar lista de empleados en orden por edad.", key="opt4")],
            [sg.Button("Salir")]
        ]
    return menuPrincipal

def defineMenuReg():
    menuRegistro = [
            [sg.Text("Nombre\t\t\t", background_color="#1A1A1A"), sg.In(size=(25, 1), enable_events=True, key="Name")],
            [sg.Text("Apellido Paterno\t\t", background_color="#1A1A1A"), sg.In(size=(25, 1), enable_events=True, key="AP")],
            [sg.Text("Apellido Materno\t\t", background_color="#1A1A1A"), sg.In(size=(25, 1), enable_events=True, key="AM")],
            [sg.Text("Fecha de nacimiento\t", background_color="#1A1A1A"), sg.In(size=(25, 1), enable_events=True, key="FN")],
            [sg.Button(button_text="Registrar")],
            [sg.Button(button_text="Regresar", key="R1")]
        ]
    return menuRegistro

def defineMenuEdadPorID():
    menuEdadPorID = [
            [sg.Text("Introduzca un ID"), sg.In(size=(25, 1), enable_events=True, key="BPID")],
            [sg.Text("", background_color="#1A1A1A", key="contEdad")],
            [sg.Button(button_text="Buscar")],
            [sg.Button(button_text="Regresar", key="R2")]
        ]
    return menuEdadPorID

def defineMenuOrdApe():
    menuOrdPorAP = [
            [sg.Text("", background_color="#4a4a4a", key="ordAlf")],
            [sg.Button(button_text="Regresar", key="R3")]
        ]
    return menuOrdPorAP

def defineMenuOrdEdad():
    menuOrdPorEdad = [
            [sg.Text("", background_color="#4a4a4a", key="ordEdad")],
            [sg.Button(button_text="Regresar", key="R4")]
        ]
    return menuOrdPorEdad

# funcion para registrar los empleados
def registrarEmpleado(contadorID, Nombre, ApeP, ApeM, FechNac, valid):
    valid = validName(Nombre, valid)
    if (valid == False):
        sg.Popup('Nombre no valido', keep_on_top=True, background_color="#1A1A1A")
        return valid
    valid = False

    valid = validName(ApeP, valid)
    if (valid == False):
        sg.Popup('Apellido Paterno no valido', keep_on_top=True, background_color="#1A1A1A")
        return valid
    valid = False

    valid = validName(ApeM, valid)
    if (valid == False):
        sg.Popup('Apellido Materno no valido', keep_on_top=True, background_color="#1A1A1A")
        return valid
    valid = False

    valid = validarFecha.validar(FechNac)
    if (valid == False):
        sg.Popup('Fecha de nacimiento no valida', keep_on_top=True, background_color="#1A1A1A")
        return valid
    if (valid == True):
        if (calcEdad(FechNac) < 18):    # si el solicitante tiene menos de 18 años no se acepta
            valid = False
            sg.Popup('Menor de edad', keep_on_top=True, background_color="#1A1A1A")
            return valid

    return valid   # Se retorna el formulario validado

# funcion para validar el nombre
def procNom(nombre):
    return nombre.lower().title().strip()

def validName(nombre, valid):
    cont = 0    # variable para contar los caracteres alfanumericos
    if (all(x.isalpha() or x.isspace() for x in nombre) and len(nombre) >= 2):  # se toma en cuenta que contenga solo espacios
        for x in nombre:                                                        # y caracteres alfanumericos ademas de un tamaño mayor a dos
            if (x.isalpha() == True):                                           # se cuentan los caracteres alfanumericos para comprobar que minimo sean 2
                cont += 1

    if (cont >= 2):     # si se cumplen todas las condiciones se valida
        valid = True

    return valid

# funcion para obtener la edad
def obtenerEdadPorID(empleados, contadorID, valor):
    ID = 0
    edad = 0            # variable para almacenar la edad
    if (valor.isnumeric() == True):   # si el ID es validamente numerico se acepta
        ID = int(valor)
        if (ID >= contadorID):       # si el ID entra en el rango de IDs existentes se valida
            sg.Popup('El ID no existe, fuera de rango.', keep_on_top=True, background_color="#1A1A1A")
            return 0
    else:
        sg.Popup('No es un ID valido', keep_on_top=True, background_color="#1A1A1A")
        return 0
    edad = calcEdadProc(empleados[ID].FechNac)  # se llama a la funcion para calcular la edad
    return edad

# Funcion para calcular la edad
def calcEdad(fecha):
    presente = date.today() # se pide la fecha actual

    day = int(fecha[0:2])   # se disecciona la fecha de nacimiento en dia, mes y año
    month = int(fecha[3:5])
    year = int(fecha[6:10])
    FechNac = date(year, month, day)    # se convierte en una fecha para trabajar

    edad = presente.year - FechNac.year - ((presente.month, presente.day) < (FechNac.month, FechNac.day)) # se calcula la edad
    return edad # se retorna la edad

def calcEdadProc(fecha):
    presente = date.today() # se pide la fecha actual

    edad = presente.year - fecha.year - ((presente.month, presente.day) < (fecha.month, fecha.day)) # se calcula la edad
    return edad # se retorna la edad

# Funcion para desplegar los empleados en orden alfabetico por el apellido
def ordenAlfabetico(empleados): 
    listaOrdenada = sorted(empleados, key = operator.attrgetter('ApeP'))    # se ordena una lista auxiliar para no alterar la original en base al apellido paterno
    return listaOrdenada

# Funcion para desplegar los empleados en orden por cumpleaños
def ordenEdad(empleados):
    listaOrdenada = sorted(empleados, key = operator.attrgetter('FechNac')) # se ordena una lista auxiliar en base a la fecha de nacimiento
    return listaOrdenada

# Funcion para limpiar la consola
def limpiarPantalla():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


if __name__ == "__main__":
    main()

