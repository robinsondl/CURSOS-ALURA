'''Sara está participando de um concurso de escrita, e uma das regras exige que cada palavra de seu texto tenha um limite máximo de caracteres.

Ajude Sara criando uma função que receba uma palavra e exiba a quantidade de caracteres.

Exemplo de entrada:
Digite uma palavra: tecnologia 

Saída esperada:
Essa palavra tem 10 caracteres. '''

print('Exercício 2.- Faça como eu fiz: contador de caracteres')

def contador_palavra(caracteres):
    return len(caracteres)

palavra = input('Digite qualquer paralvra: ')
contador = contador_palavra(palavra)

print(f'Sua palavra {palavra} tem {contador} caracteres.')


'''def contar_caracteres(palavra): 
    return len(palavra) 
 
texto = input("Digite uma palavra: ") 
print(f"Essa palavra tem {contar_caracteres(texto)} caracteres.") '''