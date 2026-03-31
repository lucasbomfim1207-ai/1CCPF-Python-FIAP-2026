#Lógica E (and)
verifica_email = True
verifica_senha = False

verifica_login = verifica_email and verifica_senha
print(verifica_login)

#Lógica OU (or)
logica_ou = False or False or True
print(logica_ou)

#Lógica Not
negacao = not True
print(negacao)

if not verifica_login:
    print("Loga")
else:
    print("Entra")