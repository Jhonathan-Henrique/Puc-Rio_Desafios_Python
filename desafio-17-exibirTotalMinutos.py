#função
def converteSeg(h, m):
    return h * 60 + m

  
#Bloco principal
horas = int(input('Digite o total de horas: '))
minutos = int(input('Digite o total de minutos: '))
total = converteSeg(horas, minutos)
print(f'Total em minutos: {total}')

