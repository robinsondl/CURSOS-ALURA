import os

def exibir_exercicio():
    print('Exercício 1 e 2.\n');

dados_user = {'nome':'Robinson', 
               'idade':24, 
               'cidade':'São Paulo'};

def voltar_ao_menu_principal():
    input('Tecle ENTER para voltar ao menu!');
    main();

def opcao_invalida():
    print('Opção escolhida foi inválida!');
    voltar_ao_menu_principal();

def trocar_nome_user():
    print(f"\nO nome de usuário atual é {dados_user['nome']}. Qual o novo nome que você deseja inserir?");
    novo_nome = input('Digite o novo nome: ');

    if novo_nome != dados_user['nome']:
        dados_user['nome'] = novo_nome;
        print('Nome alterado com sucesso!');
    else:
        print('Você digitou o mesmo nome!');

    voltar_ao_menu_principal();

def trocar_idade_user():
    print(f"\nA idade atual do usuário é {dados_user['idade']}. Qual a nova idade que você deseja inserir?");
    nova_idade = int(input('Digite a nova idade: '));

    if nova_idade != dados_user['idade']:
        dados_user['idade'] = nova_idade;
        print('Idade alterada com sucesso!')
    else:
        print('Você digitou a mesma idade!')

    voltar_ao_menu_principal();

def trocar_cidade_user():
    print(f"\nA cidade atual do usuário é {dados_user['cidade']}. Qual a nova cidade que você deseja inserir?");
    nova_cidade = input('Digite a nova cidade: ');

    if nova_cidade != dados_user['cidade']:
        dados_user['cidade'] = nova_cidade;
        print('Cidade alterada com sucesso!');
    else:
        print('Você digitou a mesma cidade!');
    
    voltar_ao_menu_principal();

def opcao_escolhida():
    try:
        exibir_opcao_de_alteracao = int(input('\nDigite a opção que deseja mudar: '));

        if exibir_opcao_de_alteracao == 1:
            trocar_nome_user();
        elif exibir_opcao_de_alteracao == 2:
            trocar_idade_user();
        elif exibir_opcao_de_alteracao == 3:
            trocar_cidade_user();
        else:
            opcao_invalida();
    except:
        opcao_invalida();

def exibir_opcao_de_alteracao():
    print('\nO que você deseja mudar?\n');
    print('1. Nome do user.');
    print('2. Idade do user.');
    print('3. Cidade do user.');

print('Exibindo os dados do usuário: \n');

def dados_para_mudar():
        print('Dados do usuário:')
        nome_user = dados_user['nome'];
        idade_user = dados_user['idade'];
        cidade_user = dados_user['cidade'];
        print(f'- {nome_user} | {idade_user} | {cidade_user}');


def main():
    os.system('cls');
    exibir_exercicio();
    dados_para_mudar();
    exibir_opcao_de_alteracao();
    opcao_escolhida();

if __name__ == '__main__':
    main();