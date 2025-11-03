from collections import deque

def main():
    fila_prioritaria = deque()
    fila_geral = deque()

    while True:
        print("\n=== Fila de Embarque - Aeroporto ===")
        print("1 - Adicionar passageiro à fila")
        print("2 - Embarcar passageiro")
        print("3 - Mostrar filas")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do passageiro: ")
            prioridade = input("É passageiro prioritário? (s/n): ").lower()
            if prioridade == "s":
                fila_prioritaria.append(nome)
                print(f"{nome} foi adicionado à FILA PRIORITÁRIA.")
            else:
                fila_geral.append(nome)
                print(f"{nome} foi adicionado à FILA GERAL.")

        elif opcao == "2":
            if fila_prioritaria:
                embarcado = fila_prioritaria.popleft()
                print(f"✈️ Passageiro PRIORITÁRIO embarcado: {embarcado}")
            elif fila_geral:
                embarcado = fila_geral.popleft()
                print(f"✈️ Passageiro embarcado: {embarcado}")
            else:
                print("Nenhum passageiro na fila para embarque.")

        elif opcao == "3":
            print("\n--- FILA PRIORITÁRIA ---")
            if fila_prioritaria:
                for p in fila_prioritaria:
                    print(f"- {p}")
            else:
                print("(vazia)")

            print("\n--- FILA GERAL ---")
            if fila_geral:
                for p in fila_geral:
                    print(f"- {p}")
            else:
                print("(vazia)")

        elif opcao == "4":
            print("Encerrando o programa... ✈️")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
