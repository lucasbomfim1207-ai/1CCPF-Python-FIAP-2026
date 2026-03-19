peca1 = input("Digite o nome do primeiro produto: ")
peca2 = input("Digite o nome do segundo produto: ")

qtd_peca1 = int(input(f"Digite a quantidade desejada de {peca1} você quer? "))
qtd_peca2 = int(input(f"Digite a quantidade desejada de {peca2} você quer? "))

valor_peca1 = float(input(f"Qual o valor de {peca1}? R$"))
valor_peca2 = float(input(f"Qual o valor de {peca2}? R$"))

total_peca1 = qtd_peca1 * valor_peca1
total_peca2 = qtd_peca2 * valor_peca2
valor_total = total_peca1 + total_peca2

print("-" * 40)
print(f"Subtotal {peca1}: R$ {total_peca1:.2f}")
print(f"Subtotal {peca2}: R$ {total_peca2:.2f}")
print(f"Valor total a ser pago é de R${valor_total:.2f}")
print("-" * 40)