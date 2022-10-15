def main():
    cadena = ""
    contador = 0
    cadena = input("Introduzca una cadena de caracteres.\n>")
    for x in cadena:
        if x.isnumeric():
            contador+=1
    print("la cadena '"+cadena+"' tiene "+str(contador)+" numeros")


if __name__ == "__main__":
    main()
