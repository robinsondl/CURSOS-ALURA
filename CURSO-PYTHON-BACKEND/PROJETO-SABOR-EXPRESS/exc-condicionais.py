import os;

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
