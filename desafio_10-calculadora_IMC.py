#calculadora de IMC

def classificaIMC(imc):
    if imc < 18.5:
        print('Abaixo do peso ideal!')
    elif imc < 25.0:
        print('Peso normal')
    elif imc < 30.0:
        print('Sobrepeso')
    else:
        print('Sobrepeso acentuado')


#Bloco principal
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura**2)
classificaIMC(imc)





