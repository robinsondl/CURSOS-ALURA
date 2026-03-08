'''Carlos quer monitorar seu orçamento mensal para evitar gastos excessivos. Ele estabeleceu um limite de R$ 3.000,00 para seus gastos e precisa de um programa que ajude a controlar suas despesas. O programa deve receber o total de despesas realizadas e informar se ele ultrapassou o limite ou ainda está dentro do orçamento.

Saída esperada:

Digite o total de despesas do mês (R$): 5897.58.
Atenção! Você ultrapassou o limite do orçamento.

'''

print('Exercício 5 - Controlando o orçamento mensal.\n')

despesas = float(input('Digite o total de despesas do mês: '))
orcamento = 3000.00

if despesas <= orcamento:
    print(f'Você está dentro do orçamento do mês {despesas:.2f}R$.')
else:
    print(f'Atenção! Você ultrapassou o limite do orçamento {despesas:.2f}R$.')