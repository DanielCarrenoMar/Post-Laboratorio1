from os import system

def suma_digitos_pares(numero:int) -> int:
    if numero == 0:
        return 0

    ultimo_digito = numero % 10
    
    if ultimo_digito % 2 == 0:
        return ultimo_digito + suma_digitos_pares(numero // 10)
    else:
        return suma_digitos_pares(numero // 10)

def main():
    system("cls")
    while True:
        print("suma digitos pares".center(50,"-"))
        try:
            num = int(input("Ingresa un número natural: "))
            if num < 0:
                print("El número debe ser mayor o igual a 0.")
            else:
                resultado = suma_digitos_pares(num)
                print(f"La suma de los dígitos pares de {num} es: {resultado}")
                break
        except ValueError:
            system("cls")
            print("Se espera un número natural.")

if __name__ == "__main__":
    main()
