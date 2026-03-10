import os;

'''Exercícios
1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

Criança: 0 a 12 anos;
Adolescente: 13 a 18 anos;
Adulto: acima de 18 anos.
3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
Terceiro Quadrante: os valores de x e y devem ser menores que zero;
Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
Caso contrário: o ponto está localizado no eixo ou origem.'''

print("ℍ𝕠𝕣𝕒 𝕕𝕒 𝕡𝕣𝕒́𝕥𝕚𝕔𝕒: 𝕔𝕠𝕟𝕕𝕚𝕔𝕚𝕠𝕟𝕒𝕚𝕤\n");

print("\nPrograma 1\n");

numero = int(input("Insira um número: "));

if numero % 2 == 0:
    print(f"\nNúmero {numero} é par.\n");
else:
    print(f"\nNúmero {numero} é ímpar.\n");

print("\nPrograma 2\n");

idade = int(input("Insira a sua idade: "));

if 0 <= idade <= 12:
    print(f"\nVocê tem {idade} anos, você é uma criança!");
elif 13 <= idade <= 18:
    print(f"\nVocê tem {idade} anos, você é um adolescente!");
else:
    print(f"\nVocê tem {idade} anos, você é um adulto!");

print("\nPrograma 3\n");

def finalizar_app():
    os.system("cls"); #para windowns
    #os.system("clear") para mac
    print("\nNome de usuário ou senha inválida, por questões de SEGURANÇA, o programa foi finalizado!");

nome_user = input("Nome de Usuário: ");
senha_user = input("Senha de Usuário: ");

if nome_user == "Robinson Dahrog" and senha_user == "1A2B3C":
    print("\nParabéns, você logou com sucesso!!");
else:
    finalizar_app();

print("\nPrograma 4\n");

print("Vamos descobrir em qual quadrante do plano cartesiano o ponto se encontra, para isso: \n")

x = float(input("Insira a coordenada X: "));
y = float(input("Insira a coordenada Y: "));

if x > 0 and y > 0:
    print("O ponto está localizado no Primeiro Quadrante!");
elif x < 0 and y > 0:
    print("O ponto está localizado no Segundo Quadrante!");
elif x < 0 and y < 0:
    print("O ponto está localizado no Terceiro Quadrante!");
elif x > 0 and y < 0:
    print("O ponto está localizado no Quarto Quadrante!");
else:
    print("O ponto está localizado no Eixo ou Origem.");
