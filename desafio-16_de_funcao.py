def somaAlgorismos(n):
    return n // 10 + n % 10

def criarSenha(dia,mes,ano):
    parte1 = somaAlgorismos(dia)
    parte2 = somaAlgorismos(mes)
    parte3 = somaAlgorismos(ano % 100)
    return str(parte1) + str(parte2) + str(parte3)

#Bloco principal - testes

print(somaAlgorismos(17))
print(somaAlgorismos(9))
print(criarSenha(17, 12, 1921))
print(criarSenha(9, 5, 2024))
