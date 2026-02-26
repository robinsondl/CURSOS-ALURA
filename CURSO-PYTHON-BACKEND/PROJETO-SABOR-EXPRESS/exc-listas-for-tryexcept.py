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

def listar_numeros():
    exibir_subtitulos("Listando números: \n");
    for numero in lista_numeros:
        print(f".{numero}");

def listar_nomes():
    exibir_subtitulos("Listando nomes: \n");
    for nome in lista_nomes:
        print(f".{nome}");

def listar_nascimento():
    exibir_subtitulos("Lista de nascimentos: \n");
    for nascimento in lista_nascimento:
        print(f".{nascimento}");

def voltar_ao_menu_principal():
    input("\nPrecione ENTER para voltar ao meu principal");
    main()

def escolher_opcoes():
    try:
        opcao_escolhida = int(input("\nEscolha umas das Listas: "));

        if opcao_escolhida == 1:
            listar_numeros();
            voltar_ao_menu_principal();
        elif opcao_escolhida == 2:
            listar_nomes();
            voltar_ao_menu_principal();
        elif opcao_escolhida == 3:
            listar_nascimento();
        voltar_ao_menu_principal();
    except:
        opcao_invalida();
        voltar_ao_menu_principal();

def voltar_ao_menu_principal():
    input("\n Digite qualquer tecla para voltar ao menu principal ");
    main();

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma das opções: "));
        if opcao_escolhida == 1:
            lista_numeros();
        elif opcao_escolhida == 2:
            lista_nomes();
        elif opcao_escolhida == 3:
            lista_nascimento();
        else:
            opcao_invalida();
    except:
        opcao_invalida();


def main():
    os.system("cls");
    exibir_opcoes();
    escolher_opcoes();

if __name__ == '__main__':
    main();