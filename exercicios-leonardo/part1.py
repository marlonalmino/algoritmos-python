# Faça um Programa que solicite a temperatura em graus Celsius e a transforme em graus Fahrenheit exibindo na tela.

# celsius = float(input('\nInforme os graus em Celsius: '))
# fahrenheit = celsius * 1.8 + 32
# print(f'{celsius} °C são {fahrenheit} °F')


# Sabendo que o dólar comercial está a ( R$ 5,49 ) na cotação do dia 
# Faça um programa que leia o dinheiro que possui na carteira em ( R$ Real ) e converta para ( $ Dólar )

# carteira = float(input('Digite quanto de dinheiro na carteira você tem: '))

# print(f'Você tem R$ {carteira} ou $ {carteira / 5.49:.2f}')


# Desenvolve um programa que leia um número com até 4 casas decimais
# e que retorne informando qual é o número de cada casa decimal.
# Exemplo: 1258
# Milhar: 1
# Centena: 2
# Dezena: 5
# Unidade: 8

# Acho que ainda dá pra melhorar com while ou for

# number = input('Digite um número para ver as casas decimais: ')

# number = number[::-1]
# tamanho = number.__len__()

# if tamanho >= 4:
#     milhar = number[3]
#     centena = number[2]
#     dezena = number[1]
#     unidade = number[0]
# elif tamanho == 3:
#     milhar = 0
# elif tamanho == 2:
#     centena = 0
# elif tamanho == 1:
#     dezena = 0
# else:
#     print('Número inválido')

# print(f'\n Milhar: {milhar}\n Centena: {centena}\n Dezena: {dezena}\n Unidade: {unidade}')


# Código - Rafa Aquino

# numero = input("Insira um numero: ")
# b = len(numero)
# c = 0 
# while c != b:
#     print(numero[c])
#     c += 1


# Código - Gustavo (melhorado)

# number = int(input("Informe um número: "))

# unidade = number // 1 % 10
# dezena = number // 10 % 10
# centena = number // 100 % 10
# milhar = number // 1000 % 10

# print(f'\n Milhar: {milhar}\n Centena: {centena}\n Dezena: {dezena}\n Unidade: {unidade}')


# Código - Harry

# while True:
#     try:
#         num = int(input('Insira um número com até 4 casas decimais: '))
#         assert num <= 9999
#     except:
#         print('Valor inválido, tente novamente...')
#         continue

#     mil = 0
#     cent = 0
#     dez = 0
#     uni = 0
#     if(num >= 1000):
#         mil = num // 1000
#         num -= mil*1000
#     if(num >= 100):
#         cent = num // 100
#         num -= cent*100
#     if(num >= 10):
#         dez = num // 10
#         num -= dez*10
#     if(num >= 1):
#         uni = num
    
  
#     print(f'Milhar: {mil} \nCentena: {cent} \nDezena: {dez} \nUnidade: {uni}')
#     break