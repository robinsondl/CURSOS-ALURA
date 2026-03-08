'''Lucas trabalha em TI e precisa garantir que a temperatura de uma sala de servidores não ultrapasse 25°C. Ele quer um programa que receba a temperatura atual como entrada e, se necessário, exiba uma mensagem de alerta.

Saída esperada:

Digite a temperatura atual: 30
Alerta! Temperatura acima do limite permitido.'''

print('Exercício 3 - Temperatura dos servidores.\n')

temp = float(input('Digite a temperatura atual: '))

if temp <=25:
    print(f'\nA temperatura atual {temp}°C é recomendada!')
else:
    print(f'\nAlerta! Temperatura {temp}°C acima do limite permitido.')