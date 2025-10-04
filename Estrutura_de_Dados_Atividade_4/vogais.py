palavra = input("Digite uma palavra: ")

vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

contador_vogais = 0
for letra in palavra:
    if letra in vogais:
        contador_vogais += 1

print(f"A palavra '{palavra}' possui {contador_vogais} vogais")