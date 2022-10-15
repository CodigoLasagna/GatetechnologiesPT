def main():
    valid = True    # Variable que comprobara si la fecha pasa la validacion
    date = ""       # Variable para guardar la fecha
    date = input("Introduzca una fecha con el siguiente Formato dd/MM/yyyy\n>") # pedir fecha
    valid = validar(valid, date) # validar fecha

    if (valid):
        print("La fecha '"+date+"' Es valida")
    else:
        print("La fecha '"+date+"' Es invalida")

def validar(valid, date):
    day, month, year = 0,0,0 # Variables para guardar cada dato

    if (len(date) != 10): #comprobar que la fecha cumpla con el tamaño de la 
        valid = False
    else:
        if (date[2] != '/' or date[5] != '/'): # comprobar los separadores correctos
            valid = False

        if (not(date[0:2].isnumeric() and date[3:5].isnumeric() and date[6:10].isnumeric())): #validar que sean datos numericos
            valid = False
        else:
            day = int(date[0:2])    # Guardar dia, mes y año
            month = int(date[3:5])
            year = int(date[6:10])
            valid = validBisiesto(day, month, year, valid) # comprobar si un año es bisiesto
            if (day <= 0 or day > 31):      #comprobar que los dias, meses y años sean mayores que 0
                valid = False
            if (month <= 0 or month > 12): # Comprobar que el mes no sea mayor a 12
                valid = False
            if (year <= 0):
                valid = False

            if ((month%2) == 0): # Validar cuando un mes tiene 30 o 31 dias
                if (month <= 7):
                    if (day > 30):
                        valid = False   # asi que aquí se retira la condicion
            else:
                if (month > 7):
                    if (day > 30):
                        valid = False   # asi que aquí se retira la condicion
    return valid

def validBisiesto(day, month, year, valid):
    bisiesto = False # variable para ver si es año bisiesto
    if ((year%4) == 0):             # comprobar que un año sea bisiesto si
        if (not((year%100) == 0)):  # es divisible entre 4 pero no entre 100
            print("Año bisiesto\n")
            bisiesto = True

    if (month == 2):
        if (bisiesto == False):
            if (day > 28): # febrero en año normal son 28 dias
                valid = False
        else:
            if (day > 29):
                valid = False
    return valid

if __name__ == "__main__":
    main()
