#calculadora de IMC

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura**2)
print(f'IMC = {imc:.2f}')