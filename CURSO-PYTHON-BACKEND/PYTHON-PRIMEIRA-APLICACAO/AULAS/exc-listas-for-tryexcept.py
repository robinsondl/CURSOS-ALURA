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
    print("\nOpção Inválida!!\n");

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
    main();

def tabuada_1_a_10():
    exibir_subtitulos("Tabuada do 1 ao 10\n");

    try:
        numero = int(input("Escolha um número entre 1 e 10: \n"));

        if numero < 1 or numero > 10:
            print("\nEscolha um número entre 1 e 10: \n");
            return
        
        print(f"Tabuada do {numero}\n");
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}");
    except:
        print("\nDigite um número válido!");

def somar_pares():
    soma = 0
    for n in lista_numeros:
        if n % 2 == 0:
            soma += n
    return soma;

def somar_impares():
    soma = 0
    for n in lista_numeros:
        if n % 2 != 0:
            soma += n
    return soma;

def media_lista():
    return sum(lista_numeros) / len(lista_numeros);

def ordem_decrescente():
    lista_numeros.reverse();
    return lista_numeros;

def menu_somas():
    exibir_subtitulos(f"Lista de números: {lista_numeros}\n");
    print("Você quer somar: ");
    print("1. Pares");
    print("2. Ímpares");
    print("3. Somar todos");
    print("4. Ordem Decrescente");
    print("5. Tabuada 1 ao 10");
    print("6. Média da lista");
    print("7. Voltar ao menu principal. \n");

    try:
        escolha = int(input("Escolhar uma das opções."));

        if escolha == 1:
            resultado = somar_pares();
            print(f"\nA soma dos números pares da lista é igual a: {resultado}");
        elif escolha == 2:
            resultado = somar_impares();
            print(f"\nA soma dos números ímpares da lista é igual a: {resultado}");
        elif escolha == 3:
            resultado = sum(lista_numeros);
            print(f"\nA soma de todos os números da lista é igual a: {resultado}");
        elif escolha == 4:
            resultado = ordem_decrescente();
            print(f"A ordem decrescente da lista é igual a: {resultado}");
        elif escolha == 5:
            resultado = tabuada_1_a_10();
        elif escolha == 6:
            resultado = media_lista();
        elif escolha == 7:
            return
        else: 
            opcao_invalida();
    except:
        opcao_invalida();

def escolher_opcoes():
    try:
        opcao_escolhida = int(input("\nEscolha uma das Listas: "));

        if opcao_escolhida == 1:
            menu_somas();
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