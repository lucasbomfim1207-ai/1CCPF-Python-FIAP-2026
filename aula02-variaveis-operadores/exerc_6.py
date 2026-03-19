nota_a = float(input("Digite a primeira nota do aluno: "))
nota_b = float(input("Digite a segunda nota do aluno: "))

peso_nota_a = 4
peso_nota_b = 6

media_ponderada = (nota_a * peso_nota_a)

print("-" * 40)
print(f"A média final do aluno é de {media_ponderada: .1f}")
print("-" * 40)