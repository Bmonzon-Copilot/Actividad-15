def pedir_entero(mensaje, condicion=None,
                 mensaje_error_condicion="Valor fuera de rango. Intente de nuevo."):
    while True:
        try:
            valor = int(input(mensaje))
            if condicion is not None and not condicion(valor):
                print(mensaje_error_condicion)
                continue
            return valor
        except ValueError:
            print("Error: Debe ingresar solo números enteros.")

def pedir_solo_letras(mensaje):
    while True:
        texto = input(mensaje)
        if texto.strip() == "":
            print("Error: No puede estar vacío.")
            continue
        if not texto.isalpha():
            print("Error: Solo se permiten letras (sin espacios, números ni símbolos).")
            continue
        return texto

def pedir_caracter_letra(mensaje):
    while True:
        ch = input(mensaje)
        if len(ch) != 1:
            print("Error: Ingrese solo un carácter.")
            continue
        if not ch.isalpha():
            print("Error: Solo se permite una letra (A-Z).")
            continue
        return ch


def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)

def cadena_repetida(palabra, veces):
    if veces == 0:
        return ""
    else:
        return palabra + cadena_repetida(palabra, veces - 1)

def cuenta_letras(cadena, letra):
    if not cadena:
        return 0
    return (1 if cadena[0].lower() == letra.lower() else 0) + cuenta_letras(cadena[1:], letra)

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
        print("3. Cuenta cuántas veces aparece una letra")
        print("4. Conversión de decimal a binario")
        print("5. Calcula cuántos dígitos tiene un número")
        print("6. Salir")
        print("-" * 40)

        opcion = input("Elija una opción: ")

        match opcion:
            case "1":
                print("\n--- MÁXIMO COMÚN DIVISOR ---")
                a = pedir_entero("Ingrese el primer número: ")
                b = pedir_entero("Ingrese el segundo número: ")
                print(f"\nEl MCD de {a} y {b} es: {mcd(a, b)}\n")

            case "2":
                print("\n--- REPETIR PALABRA ---")
                palabra = pedir_solo_letras("Ingrese la palabra (solo letras): ")
                veces = pedir_entero(
                    "¿Cuántas veces quiere repetirla?: ",
                    condicion=lambda x: x >= 0,
                    mensaje_error_condicion="Error: Debe ser un entero mayor o igual a 0."
                )
                print(f"\nResultado: {cadena_repetida(palabra, veces)}\n")

            case "3":
                print("\n--- CONTAR LETRAS ---")
                cadena = pedir_solo_letras("Ingresa la cadena (solo letras): ")
                letra = pedir_caracter_letra("Ingresa la letra a buscar: ")
                print(f"\nLa letra '{letra}' aparece {cuenta_letras(cadena, letra)} veces.\n")

            case "4":
                print("\n--- DECIMAL A BINARIO ---")
                numero = pedir_entero("Ingresa un número decimal: ")
                print(f"\nBinario: {binario_decimal(numero)}\n")

            case "5":
                print("\n--- CANTIDAD DE DÍGITOS ---")
                numero = pedir_entero("Ingrese un número: ")
                print(f"\nEl número tiene {calcula_digitos(numero)} dígitos.\n")

            case "6":
                print("\n¡Gracias por usar el programa! Hasta luego.\n")
                break

            case _:
                print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()
