produto = float(input("Digite o valor do produto R$"))
valor_pago = float (input("Digite o valor que o cliente pagou R$"))

troco = valor_pago - produto

if troco > 0:
    print(f"O valor do troco é de R${troco}")
elif troco == 0:
    print("Não será necessário troco")
else:
    falta = abs(troco)
    print(f"Valor insuficiente, ainda faltam R${falta:.2f}")