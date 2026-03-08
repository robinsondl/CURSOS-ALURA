'''Camila está organizando um projeto e precisa calcular o tempo total necessário para concluir três atividades: A, B e C. No entanto, se alguma atividade tiver um número de dias negativo, o código deve avisar que os valores inseridos são inválidos e não calcular o total.

Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto. Se algum valor for negativo, mostre uma mensagem informando o erro.

Saída esperada:

Informe os dias para a atividade A: 5
Informe os dias para a atividade B: -8
Informe os dias para a atividade C: 10
Erro: Os dias não podem ser negativos'''

print('Exercício 2 - Calculando o tempo total de projeto.\n')

atvA = int(input('Informe o dia para a atividade A: '))
atvB = int(input('Informe o dia para a ativdade B: '))
atvC = int(input('Informe o dia para a ativadade C: '))
zero = 0

if atvA >= zero and atvB >= zero and atvC >= zero:
    print(f'\nO tempo real informado para concluir as 3 atividades são: {atvA + atvB + atvC} sendo assim positivos.')
else:
    print('\nErro: Os dias não podem ser negativos')
