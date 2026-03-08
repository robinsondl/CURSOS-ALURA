'''Fernanda está planejando uma viagem e quer calcular quanto pagará de pedágio. O valor do pedágio depende da distância percorrida:

Até 100 km: R$ 10,00
Entre 100 km e 200 km: R$ 20,00
Acima de 200 km: R$ 30,00
Crie um programa que receba a distância percorrida e informe o valor do pedágio correspondente.

Saída esperada:

Digite a distância percorrida (em km): 250
Valor do pedágio: R$ 30.00

'''

print('Exercício 8 - Calculando pedágio.\n')

distancia = float(input('Digite qual foi a distância percorrida: '))

dez = 10.00
vinte = 20.00
trinta = 30.00

if distancia <= 100:
    print(f'A distância percorrida foi de: {distancia:.2f}km - Valor do pedágio: {dez:.2f}R$.')
elif  100 < distancia <= 200:
    print(f'A distância percorrida foi de: {distancia:.2f}km - Valor do pedágio: {vinte:.2f}R$.')
else:
    print(f'A distância percorrida foi de: {distancia:.2f}km - Valor do pedágio: {trinta:.2f}R$.')