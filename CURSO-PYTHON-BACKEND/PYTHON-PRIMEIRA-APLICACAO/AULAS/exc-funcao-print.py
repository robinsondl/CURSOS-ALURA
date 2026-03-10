#Link para a Letra: https://fsymbols.com/
'''Exercícios
1 - Imprima a frase: Python na Escola de Programação da Alura.

2 - Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.

3 - Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha, como mostrado a seguir:

A
L
U
R
A

4 - Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de pi precisa ser armazenado em uma variável e arredondado para apenas duas casas decimais. Para facilitar, utilize:

pi = 3.14159'''

print('Exercício 1.\n')

print("""
𝓟𝓨𝓣𝓗𝓞𝓝 𝓝𝓐 𝓔𝓢𝓒𝓞𝓛𝓐 𝓓𝓔 𝓟𝓡𝓞𝓖𝓡𝓐𝓜𝓐𝓒̧𝓐̃𝓞 𝓐𝓛𝓤𝓡𝓐
""");

print('\nExercício 2.\n')

nome = input("Qual o seu nome: ");
idade = input("Quantos anos você tem: ")

print(f"""\nObrigado por se apresentar! Agora sei que seu nome é {nome} e você tem {idade} anos.Seja bem vindo!""")

print('\nExercício 3.\n')

#print("""
#A
#L
#U
#R
#A
#""")

print("\nA","L","U","R","A\n", sep= "\n")

print('\nExercício 4.\n')

pi_arredondado = 3.14159

print(f"O valor de pi é {pi_arredondado:.2f}!")