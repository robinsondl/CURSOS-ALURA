'''Bruno gerencia um pequeno comércio e quer saber qual produto teve o melhor desempenho de vendas no mês passado. Ele registrou a quantidade vendida de dois produtos: maçãs e bananas. Agora, ele precisa escrever um programa que identifique e exiba qual deles teve maior venda.

Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando qual deles vendeu mais. Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.

Saída esperada:

Digite a quantidade de maças vendidas: 15
Digite a quantidade de bananas vendidas: 3
As maças tiveram mais vendas.

Você conseguiu implementar? Compartilhe com a gente no fórum!'''

print('Exercício 1 - Monitorando vendas no comércio.\n')

maca = int(input('Digite a quantidade de maças vendidas: '))
banana = int(input('Digite a quantidade de bananas vendidas: '))

if maca > banana:
    print(f'\nA quantidade de maças vendidas {maca} foi superior a de bananas vendidas {banana}.')
elif banana > maca:
    print(f'\nA quantidade de bananas vendidas {banana} foi superior a de maças vendidas {maca}.')
else:
    print(f'\nA quantidade de vendas foram iguais.')