# Crie a função somaAlgarismos, que receba como parâmetro um número inteiro de 2 algarismos e retorne a soma de seus algarismos; se, por exemplo, a função receber o inteiro 27, deve retornar 9;
# Faça dois testes com a função somaAlgarismos utilizando os valores 17 e 9;
# Crie a função criaSenha, que receba três números inteiros como parâmetros representando uma data de nascimento (dia, mes e ano) e retorne a string resultante da concatenação da soma dos algarismos
#  do dia com a soma dos algarismos do mês com a soma dos dois últimos algarismos do ano; para calcular cada soma, utilize a função somaAlgarismos; se, por exemplo, a função receber os números 17, 12 e 1921, deverá retornar a string 833.
# Faça dois testes com a função criaSenha utilizando os valores:
# 17, 12 e 1921;
# 9, 5, 2024.

def somaAlgorismos(numero):
    dezenas = numero // 10
    unidade = numero % 10
    return dezenas + unidade

print(somaAlgorismos(9))
