def main():
    date = ""       # Variable para guardar la fecha
    valid = True    # Variable que comprobara si la fecha pasa la validacion
    length = 0    #
    contador = 0

    date = input("Introduzca una fecha con el siguiente Formato dd/MM/yyyy\n>")
    value = ""
    dataVal = 0
    length = len(date)

    if (length != 10):
        valid = False
    else:
        for i in range(length):
            if (i == 2 or i == 5):
                value = ""
                if (date[i] != '/'):
                    valid = False
            else:
                value += date[i]
            if (len(value) == 2 or len(value) == 4):
                contador += 1
                dataVal = int(value)
                if (dataVal <= 0):
                    valid = False
                if (contador == 1):
                    if (dataVal > 31):
                        valid = False
                if (contador == 2):
                    if (dataVal > 12):
                        valid = False
                if (contador == 4):
                    print(dataVal)



    if (valid):
        print("La fecha '"+date+"' Es valida")
    else:
        print("La fecha '"+date+"' Es invalida")



if __name__ == "__main__":
    main()
