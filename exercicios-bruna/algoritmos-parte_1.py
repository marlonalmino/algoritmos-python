# Faça um programa que imprima duas notas e calcule a média aritmética.

# nota_um = float(input('Digite a primeira nota: '))
# nota_dois = float(input('Digite a segunda nota: '))
# print(f'A média é: {(nota_um + nota_dois) / 2}')


# Solicite ao usuário que informe um número inteiro e informe se o número é positivo, negativo ou neutro.

# try:
#     number = int(input('Informe um número: '))
# except:
#     print('Inválido, insira um número!')
# if number == 0:
#     print(f'O número {number} é neutro!')
# elif number > 0:
#     print(f'O número {number} é positivo!')
# else:
#     print(f'O número {number} é negativo!')


# Uma empresa te contratou como programador e a sua primeira tarefa é: Criar um programa que solicite ao usuário 
# a senha e solicite que digite-a novamente até que as duas sejam digitadas da mesma forma.

# username = input('Digite seu nome de usuário: ')
# print(f'Seja bem-vindo {username}!')
# senha = input('Digite a senha: ')
# confirmacao_senha = input('Confirme sua senha: ')

# while senha != confirmacao_senha: 
#     print('\nSenhas diferentes!')
#     senha = input('Digite uma senha: ')
#     confirmacao_senha = input('Confirme sua senha: ')
# else:
#     print('\nSucesso!')


# Faça um programa que solicite um número inteiro e mostre a tabuad de multiplicação de 1 a 10 do valor informado.

# numero_tabuada = int(input('Informe o número para ver a tabuada: '))
# for index in range(1,11):
#     print(f'{numero_tabuada} x {index} = {numero_tabuada * index}')


# Na matemática, a sucessão de Fibonacci , é uma sequência de números inteiros, começando normalmente por 0 e 1, na 
# qual cada termo subsequente corresponde à soma dos dois anteriores. Crie um programa que leia um número e o imprima na sequência de Fibonacci.

# anterior = 0
# proximo = 0
# number = int(input('Digite um número para fibonacci: '))

# while proximo < number:
#     print(proximo)
#     proximo += anterior
#     anterior = proximo - anterior
    
#     if proximo == 0:
#         proximo += 1


#  Faça um programa que informe um número inteiro e calcule a soma de todos os números de 1 até o número digitado.Por exemplo:

# numero_soma = int(input('Digite um inteiro: '))
# result = 0
# for index in range (1, numero_soma+1):
#     print(f'\nO número atual é: {index}')
#     result += index
#     print(f'A soma atual é: {result}')

# print('\nO resultado final é:', result)

# Código do Rafael

# numero = int(input("Insira um número: "))
# lista = []
# for n in range(1,numero + 1):
#     lista.append(n)
# print(lista)
# print(sum(lista))


# Todo ano há reajuste salário e a tabela do próximo ano está na tabela abaixo. Faça um programa que calcule o reajuste do funcionário 
# de acordo com o salário atual.
# Salário atual	            Reajuste
# Abaixo de R$ 700	        12%
# de R$ 700 até R$1200	    10%
# Acima de R$1200	        5%

# salario_atual = float(input('Para verificar o reajuste, informe seu salário atual: R$ '))
# if salario_atual <= 0:
#     print('Salário inválido!')
# elif salario_atual < 700:
#     print(f'Reajuste de R$ {salario_atual * 0.12}. O valor total do salário é R$ {salario_atual + (salario_atual * 0.12)}')
# elif salario_atual < 1200:
#     print(f'Reajuste de R$ {salario_atual * 0.10}. O valor total do salário é R$ {salario_atual + (salario_atual * 0.10)}')
# else:
#     print(f'Reajuste de R$ {salario_atual * 0.05}. O valor total do salário é R$ {salario_atual + (salario_atual * 0.05)}')