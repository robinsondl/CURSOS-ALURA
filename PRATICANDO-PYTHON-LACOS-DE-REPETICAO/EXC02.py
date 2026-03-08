'''André está testando um novo recurso no backend do Buscante que processa dados em um loop. Durante os testes, ele percebeu que o sistema parou de responder, e suspeita que o problema está em um loop infinito.

contador = 0

while contador < 10:
    print("Processando dados...")'''

print('Exercício - 2 O que é um loop infinito?')

contador = 0

while contador < 10:
    print(f"Processando dados... Step {contador}")
    contador += 1 #Esse caro ataliza o contador+1, assim ele não fica em loop