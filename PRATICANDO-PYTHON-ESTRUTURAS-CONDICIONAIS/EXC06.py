'''Mariana é responsável por liberar o acesso ao escritório e precisa de um programa que verifique se os funcionários podem entrar. Para isso, ela usará o horário atual. O escritório só permite acesso entre 8h e 18h. Crie um programa que receba a hora atual como entrada (em formato de 24 horas) e exiba uma mensagem informando se o acesso é permitido ou negado.

Saída esperada:

Digite a hora atual (Formato 24 horas): 21
Acesso negado.

'''

print('Exercício 6 - Controle de acesso ao escritório.\n')

hora = float(input('Digite a hora atual: '))

limiteE = 8
limiteS = 18

if limiteE <= hora <= limiteS:
    print(f'Horário de entrada: {hora:.2f} HRS - Acesso permitido.')
else:
    print(f'Horário de entrada: {hora:.2f} HRS - Acesso negado!')