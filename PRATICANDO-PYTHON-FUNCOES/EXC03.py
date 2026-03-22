'''Beatriz está desenvolvendo um sistema de atendimento para um site de serviços. Ela deseja criar um programa que exiba uma saudação personalizada dependendo da hora do dia que o usuário acessa a plataforma. O sistema deverá ter a seguinte regra:

Se for antes das 12h, exibir "Bom dia";

Entre 12h e 18h, exibir "Boa tarde";

Após 18h, exibir "Boa noite".

Exemplo de entrada:
Digite a hora atual (0-23): 15 

Saída esperada:
Boa tarde! 
'''

print('Exercício 3. - Faça como eu fiz: saudação personalizada')

def hora_inserida(horario):
    if 00 <= horario <=5:
        horario = f'Boa madrugada! Agora são {horario}'
    elif 6 <= horario < 12:
        horario = f'Bom dia! Agora são {horario}'
    elif 12 <= horario < 18:
        horario = f'Boa tarde! Agora são {horario}'
    elif 18 <= horario <= 23:
        horario = f'Boa noite! Agora são {horario}'
    else:
        horario = 'Hora inválida!'
    return horario

hora = int(input('Digite a hora atual (00-23): '))

print(hora_inserida(hora))