qtd_livros = 3
qtd_caneta = 2

preco_livro = 25
preco_caneta = 5

total_livros = (qtd_livros * preco_livro)
total_caneta = (qtd_caneta * preco_caneta)
total_geral = (total_caneta + total_livros)

print("-" * 40)
print(f"O total gasto com livros é de R${total_livros: .2f}")
print(f"O total gasto com canetas é de R${total_caneta: .2f}")
print(f"O total de tudo gasto é de R${total_geral: .2f}")
print("-" * 40)