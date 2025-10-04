senha_correta = "1234"

while True:
    senha_digitada = input("Digite a senha: ")
    
    if senha_digitada == senha_correta:
        print("✅ Senha correta!")
        break
    else:
        print("❌ Errooou! Tente novamente.")