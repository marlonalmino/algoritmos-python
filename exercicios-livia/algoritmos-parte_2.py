# Escreva um algoritmo para ler um valor (do teclado) e escrever (na tela) o seu antecessor.

# number = int(input('\nDigite um número para ver seu antecessor: '))
# print(f'O antecessor de {number} é {number-1}')


# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

# altura = float(input('\nDigite a altura (em metros): '))
# largura = float(input('Digite a largura (em metros): '))

# area = altura * largura
# tinta = area / 2

# print(f'\nPara uma parede com área de {area}, precisará de {tinta}L de tinta!')


# Crie um programa que solicite um nmero entre 1 e 10. Se a pessoa digitar um número diferente, deve mostrar a mensagem
# "Entrada inválida" e solicitar o número novamente. Se digitar correto, mostrar o número digitado.

# number = float(input('\nDigite um número entre 1 e 10: '))

# while number < 1 or number > 10:
#     number = float(input('Entrada inválida! Digite um número novamente: '))

# print(f'\nO número entre 1 e 10 foi: {number}')


# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

# pesos = []
# print()

# for i in range(1, 6):
#     peso = float(input(f'Digite o peso da pessoa {i}: '))
#     pesos.append(peso)

# menor = min(pesos)
# maior = max(pesos)

# print(f'\nO menor peso inserido foi {menor}kg')
# print(f'O maior peso inserido foi {maior}kg')


# Usando o nome dos seus colegas Aline, Bruna, Gustavo, Huan, Marlon, Rafa, Rafael e Victor, faça um programa que leia os
# nomes e sortei um deles para responder a próxima questão, escrevendo na tela o nome do escolhido.

# import random

# list = ['Aline', 'Bruna', 'Gustavo', 'Huan', 'Marlon', 'Rafa', 'Rafael', 'Harry']

# print(f'\nO sorteado que vai responder a questão é o {random.choice(list)}')


# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até dez. Seu programa deverá
# ler um número pelo teclado (entre 0 e 10) e mostrá-lo por extenso.

# extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')

# number = int(input('\nDigite um número inteiro entre 0 e 10: '))

# if number >= 0 and number <= 10: 
#     print(f'{number} por extenso é {extenso[number]}')
# else:
#     print('\nVocê inseriu um número fora de 0 e 10!')