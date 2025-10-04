import time

numero = int(input("Digite um número inteiro positivo: "))

print(f"\nContagem regressiva a partir de {numero}:")
print("Preparar...")

while numero >= 0:
    print(numero)
    if numero > 0:  
        time.sleep(1)  
    numero -= 1

print("Já!")