import os

lista_numeros = [1,2,3,4,5,6,7,8,9,10];
lista_nomes = ["Robinson", "Marianna", "Annairam", "Nosnibor"];
lista_nascimento = ["2002", "2003", "2026"];

def exibir_opcoes():
    print("\n1. Lista de números: ");
    print("\n2. Lista de nomes: ");
    print("\n3. Lista de datas de nascimento: ");

def exibir_subtitulos(texto):
    os.system("cls");
    print(texto);

def opcao_invalida():
    print("\nOpção Inválida!!\n")

def listas():
    exibir_subtitulos("Listando Opções");

def escolher_opcoes():
    try:
        opcao_escolhida = int(input("Escolha umas das Listas: "));

        if opcao_escolhida == 1:
            lista_numeros();
        elif opcao_escolhida == 2:
            lista_nomes();
        else:
            lista_nascimento();
    except:
        opcao_invalida();

def voltar_ao_menu_principal():
    input("\n Digite qualquer tecla para voltar ao menu principal ");
    main();



def main():
    exibir_opcoes();
    os.system("cls");

if __name__ == '__main__':
    main();