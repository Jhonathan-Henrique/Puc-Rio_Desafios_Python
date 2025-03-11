def maiorValor(n1, n2, n3):
    if n1>n2>n3:
        print(f'O valor {n1} é maior que n2 {n2} e n3 {n3}')
    elif n2>n3:
        print(f'O valor de {n2} é maior que n1 {n1} e n3 {n3}')
    else:
        print(f'O valor de n3 {n3} é o maior numero')

maiorValor(30,20,10)