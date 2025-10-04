print("--- Será que é par ou impar? ---")
print("\n")
print("Digite 'sair' a qualquer momento para encerrar o programa, beleza?")
print("\n")
while True:
    entrada_usuario = input("Digita um número aí (inteiro ou decimal, você que escolhe ou 'sair'): ")
    if entrada_usuario.lower() == 'sair':

        print("\n")
        print("Encerrando o programa. Flw V1D4 L0k4")
        break

    try:
        numero_digitado = float(entrada_usuario)
        print("\n")
        numero_inteiro = int(numero_digitado)
        print("\n")
        if numero_inteiro % 2 == 0:
            print(f"O número {entrada_usuario} é: \033[33mPAR MORÔ?\033[0m")
        else:
            print(f"O número {entrada_usuario} é: \033[32mÍMPAR MORÔ?\033[0m")
    except ValueError:
        print("Erro: IAE parça essa entrada é inválida (Lá ele). Na moral, digita um número válido aê (ex: 7, 10, 3.5) ou pede pra 'sair'.")
    except Exception as e:
        print(f"{ConnectionResetError}Erro: IAE amizade, ocorreu um erro inesperado: {e}")