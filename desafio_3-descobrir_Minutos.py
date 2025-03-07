#Escreva um programa que leia dois inteiros representando horas e minutos e exiba o total em minutos. Por exemplo, se forem lidos os valores 2 e 35, o programa deverá exibir: 155 minutos

def descobrir_Minutos(horas, minutos):
    horas = horas * 60
    return horas + minutos

print(descobrir_Minutos(2,35))