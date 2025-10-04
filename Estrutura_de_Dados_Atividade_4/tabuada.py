numero = int(input("Digite um número para ver sua tabuada: "))

print(f"\nTabuada do {numero}:")
print("-" * 15)

# Laço de repetição para calcular e mostrar a tabuada
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} × {i:2} = {resultado:2}")

print("-" * 15)