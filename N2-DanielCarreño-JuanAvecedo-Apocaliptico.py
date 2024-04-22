from os import system

def apocaliptico(numero:int, repite:int = 0) -> bool:
    if repite >= 3: return True 
    if numero == 0: return False

    mod = numero%10
    
    if mod == 6: repite += 1
    else: repite = 0

    numero = numero //10
    return apocaliptico(numero, repite)


def main():
    system("cls")
    while True:
        print("Numero Apocaliptico".center(50,"-"))
        try:
            num = int(input("Ingresa un número entero: "))
            if num > 0: break
    
        except ValueError:
            system("cls")
            print("Se espera un número entero.")

    if apocaliptico(num):
        print(f"El número {num} es apocalíptico.")
    else:
        print(f"El número {num} NO es apocalíptico.")

if __name__ == "__main__":
    main()



