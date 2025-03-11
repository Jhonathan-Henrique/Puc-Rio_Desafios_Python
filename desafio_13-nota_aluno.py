def exibeSituacao(media):
    print(f'\nMédia do aluno: {media:.1f}')
    if media >= 7.0:
        print('Aprovado')
    elif media >= 3.0:
        print('Reprovado')
    else:
        print('Em prova final')



#Bloco Principal

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print(exibeSituacao(media))