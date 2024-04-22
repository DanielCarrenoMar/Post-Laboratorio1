from os import system

def contar_ceros_binarios(n, count=0):
    if n == 0:
        return count
    
    bit = n % 2
    if bit == 0:    
        count += 1
    
    return contar_ceros_binarios(n // 2, count)

def diabolico(num):
    return contar_ceros_binarios(num) % 2 == 0

def main():
    system("cls")
    while True:
        print("Numero Diabolico".center(50,"-"))
        try:
            numero = int(input("Introduce un número entero: "))
            break
        except ValueError:
            system("cls")
            print("Por favor, ingresa un número entero válido.")

    if diabolico(numero):
        print(f"{numero} es un número diabólico.")
    else:
        print(f"{numero} no es un número diabólico.")

if __name__ == "__main__":
    main()