def mcd(a,b):
    if(b==0):
        return a
    else:
        return mcd(b,a%b)

def cadena_repetida(palabra,veces):
    if veces == 0:
        return ""
    else:
        return palabra+cadena_repetida(palabra,veces-1)

def cuenta_letras(cadena,letra):
    if not cadena:
        return 0
    return (1 if cadena[0] == letra else 0) + cuenta_letras(cadena[1:], letra)

def binario_decimal(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return binario_decimal(n // 2) + str(n % 2)

def calcula_digitos(n):
        n = abs(n)
        if n < 10:
            return 1
        return 1 + calcula_digitos(n // 10)

def menu():
    while True:
        print("\n\n" + "*" * 40)
        print("          MENU PRINCIPAL          ")
        print("-" * 40)
        print("1. Calcular MCD")
        print("2. Repetir palabra")
        print("3. Cuenta cuantas veces aparece una letra")
        print("4. Conversion de decimal a binario")
        print("5. Calcula cuantos digitos tiene un numero")
        print("6. Salir")
        print("-" * 40)

        opcion=input("Elija una Opcion: ")

        match opcion:
            case "1":
                print("\n--- MÁXIMO COMÚN DIVISOR ---")
                try:
                    a = int(input("Ingrese el primer número: "))
                    b = int(input("Ingrese el segundo número: "))
                    print(f"\nEl MCD de {a} y {b} es: {mcd(a, b)}\n")
                except ValueError:
                    print("\nError: Debe ingresar solo números enteros.\n")
            case "2":
                print("\n--- REPETIR PALABRA ---")
                palabra = input("Ingrese la palabra: ")
                veces = int(input("¿Cuántas veces quiere repetirla?: "))
                print(f"\nResultado: {cadena_repetida(palabra, veces)}\n")
            case "3":
                print("\n--- CONTAR LETRAS ---")
                cadena = input("Ingresa la cadena: ")
                letra = input("Ingresa la letra a buscar: ")
                print(f"\nLa letra '{letra}' aparece {cuenta_letras(cadena, letra)} veces.\n")
            case "4":
                print("\n--- DECIMAL A BINARIO ---")
                try:
                    numero = int(input("Ingresa un número decimal: "))
                    print(f"\nBinario: {binario_decimal(numero)}\n")
                except ValueError:
                    print("\nError: Debe ingresar solo números enteros.\n")
            case "5":
                print("\n--- CANTIDAD DE DÍGITOS ---")
                try:
                    numero = int(input("Ingrese un número: "))
                    print(f"\nEl número tiene {calcula_digitos(numero)} dígitos.\n")
                except ValueError:
                    print("\nError: Debe ingresar solo números enteros.\n")
            case "6":
                print("\n¡Gracias por usar el programa! Hasta luego.\n")
                break

menu()
