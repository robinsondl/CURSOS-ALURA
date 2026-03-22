'''Julia é professora e precisa de um programa para ajudar seus alunos a calcularem suas idades com base no ano de nascimento. Sua tarefa é criar uma função que receba o ano de nascimento e o ano atual e retorne à idade correspondente.

Exemplo de entrada:
Digite o ano de nascimento: 2005  
Digite o ano atual: 2025 

Saída esperada:
A idade é 20 anos. '''

print('Exercício 1. - Faça como eu fiz: calculando a idade')

def calculo_idade(nascimento, idade):
    return  idade - nascimento

ano_nascimento = int(input('Digite o seu ano de nascimento: '))
ano_atual = int(input('Digite o ano atual: '))

idade = calculo_idade(ano_nascimento, ano_atual)

print(f'Você tem {idade} anos.')