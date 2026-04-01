'''Hora da prática: instância de uma classe

Em uma carreira de desenvolvimento de software, a prática consistente desempenha um papel fundamental na construção de bases sólidas. Pensando nisso, criamos uma lista de atividades (não obrigatórias) focada em prática para melhorar ainda mais sua experiência de aprendizagem. Bora praticar então?
Exercícios
Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.
Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
Altere o valor do atributo nome para 'Bistrô'.
Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
Mude o estado da instância restaurante_pizza para ativo.
Imprima no console o nome e a categoria da instância restaurante_praca.'''

class Restaurante:
    nome = ''
    categoria = ''
    ativo = bool

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Só Massa Food'
restaurante_praca.categoria = 'Italiana'
restaurante_praca.ativo = True

nome_do_restaurante_praca = restaurante_praca.nome
categoria_restaurante_praca = restaurante_praca.categoria

restaurante_praca2 = Restaurante()
restaurante_praca2.nome = 'Bistrô'

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
restaurante_pizza.ativo = True

if restaurante_praca.ativo:
    print('O restaurante está ativo!')
else:
    print('O restaurante está inativo!')

if restaurante_pizza.categoria == 'Fast Food':
    print('É um Fast Food!')
else: 
    print('Não é um Fast Food!')

print(f'Nome Restaurante: {restaurante_praca.nome}, Categoria Restaurante: {restaurante_praca.categoria}, Status Restaurante: {restaurante_praca.ativo}')