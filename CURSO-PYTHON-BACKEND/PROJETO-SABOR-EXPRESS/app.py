import os

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
    os.system("cls"); #para windowns
    #os.system("clear") para mac
    print("Programa Finalizado!\n");

def escolher_opcao():
    opcao_escolhida = int(input("Escolha uma opção: "));

    #opcao_escolhida = int(opcao_escolhida)
    #print(f"\nVocê escolheu a opção, {opcao_escolhida}");
    #print(opcao_escolhida ==1);
    #print(type(opcao_escolhida));
    #print(type(1));

    if opcao_escolhida == 1:
        print("Cadastrar restaurante");
    elif opcao_escolhida == 2:
        print("Listar restaurantes");
    elif opcao_escolhida == 3:
        print("Ativar restaurante");
    else:
        finalizar_app();

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    
if __name__ == '__main__':
    main()