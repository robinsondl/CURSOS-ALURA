import os

restaurantes = ["Pizzaria", "Sushiria", "Padaria"];

def exibir_nome_do_programa():
#Link para a Letra: https://fsymbols.com/
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """);

def exibir_opcoes():
    print("1. Cadastrar restaurante");
    print("2. Listar restaurante");
    print("3. Ativar restaurante");
    print("4. Sair\n");

def finalizar_app():
    exibir_subtitulos("Programa Finalizado!\n");

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def opcao_invalida():
    print("Opção Inválida!!\n")
    voltar_ao_menu_principal();

def exibir_subtitulos(texto):
    os.system("cls");
    print(texto);

def cadastrar_novo_restaurante():
    exibir_subtitulos("Cadastro de novos restaurantes\n");
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ");
    restaurantes.append(nome_do_restaurante);
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!!")
    
    voltar_ao_menu_principal();

def listar_restaurante():
    exibir_subtitulos("Listando restaurantes\n");
    for restaurante in restaurantes:
        print(f".{restaurante}");
    
    voltar_ao_menu_principal();

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "));

        #opcao_escolhida = int(opcao_escolhida)
        #print(f"\nVocê escolheu a opção, {opcao_escolhida}");
        #print(opcao_escolhida ==1);
        #print(type(opcao_escolhida));
        #print(type(1));

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante();
        elif opcao_escolhida == 2:
            listar_restaurante();
        elif opcao_escolhida == 3:
            print("Ativar restaurante");
        elif opcao_escolhida == 4:
            finalizar_app();
        else:
            opcao_invalida();
    except:
        opcao_invalida();

def main():
    os.system("cls");
    exibir_nome_do_programa();
    exibir_opcoes();
    escolher_opcao();

if __name__ == '__main__':
    main();