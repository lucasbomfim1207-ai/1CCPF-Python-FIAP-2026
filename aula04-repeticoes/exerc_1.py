while True:
    valor = input("Digite um número entre 1 e 10: ")

    # Verificação do padrão/condição
    if int(valor) >= 1 or int(valor) <= 10:
        print("Valor aceito!")
        break  # Sai do loop quando o valor está correto
    print("Valor inválido. Tente novamente.")