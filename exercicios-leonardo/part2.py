# Faça um programa que permita ler vários números:
# Para sair do programa, será necessário digitar o número 0.
# Após sair, mostre quantos números foram digitados e qual foi a soma entre eles

# list = []
# soma = 0
# while True:
#     num = int(input("Informe o número: "))
#     if num == 0:
#         break
#     list.append(num)

# for n in list:
#     soma += n

# print(list)
# print(f"A soma dos valores é: {soma}")


# Desenvolva um programa que solicite a quantidade de dias que o veículo foi alugado
# e a quantidade kilometros percorridos.
# Sabendo que o veículo custa R$58 a diária e R$0,21 por km rodado, calcule o total gasto

# veiculo_aluguel = int(input('\nPor quantos dias o veículo foi alugado: '))
# kilometragem = float(input('Quantos km foram rodados? '))

# calc = (veiculo_aluguel * 58) + (0.21 * kilometragem)

# print(f'\nO veículo foi alugado por {veiculo_aluguel} e rodou {kilometragem}\n O total gasto foi de R$ {calc:.2f}')


# Faça um programa que permite ler um número e escolhar uma das seguintes conversões:
# 1 para binário
# 2 para octal
# 3 para hexadecimal.

# bases_binarias = {
#     1: 'binário',
#     2 : 'octal',
#     3 : 'hexadecimal'
# }

# number = int(input('Digite o número que será usado para conversão: '))
# choice = int(input('Digite: \n1 para binário \n2 para octal \n3 para hexadecimal\n'))
# convert = 0

# if choice == 1:
#     convert = format(number, 'b')
# elif choice == 2:
#     convert = format(number, 'o')
# elif choice == 3:
#     convert = format(number, 'x')
# else:
#     print('Escolha inválida!')

# print(f'\n O número normal é: {number}\n Convertido para {bases_binarias[choice]} fica: {convert}')


# Escreva um programa que leia um número e mostre o seu fatorial.
#  Exemplo: Número 5 = 5 x 4 x 3 x 2 x 1 = 120

# Melhorar o código (WIP)

# number = int(input('Digite um número para ver seu fatorial: '))
# fatorial = number

# while number >= 1:

#     if number > 0:
#         fatorial = fatorial * (number - 1)


# Código - Rafael Lima

# from math import factorial
# number = int(input('Digite um número: '))
# print(f'O resultado de {number}! é: {factorial(number)}')


# Código - Leonardo

# n1 = int(input('Digite um numero : '))

# fat = 1
# for c in range(n1, 0, -1):
#     print(c, end='')
#     print(' x 'if c > 1 else ' = ',end='')
#     fat = fat * c

# print(fat)

# Faça um programa que leia a velocidade de um veículo. Se ultrapassar 80 Km/h, reporte a mensagem informando que foi multado.
# O valor da multa é R$ 45,00 por cada Km acima do limite. Para sair do programa, será necessário digitar sair

# print('\nDigite exit para sair do programa!\n')

# while True:

#     entrada = input('Informe a velocidade do veículo em Km/h: ').upper()
    
#     if entrada == 'EXIT':
#         break

#     velocidade = float(entrada)

#     if velocidade > 80:
#         multa = (velocidade - 80) * 45
#         print(f'Você foi multado em R$ {multa:.2f}\n')