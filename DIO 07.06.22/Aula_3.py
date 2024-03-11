# VERIFICANDO MEDIA ENTRE 4 NUMEROS DIGITADOS
a = int(input('Entre com o Primeiro Bimestre: '))
if a > 10:
    a = int(input('Você digitou errado. Primeiro Bimestre: ' ))
b = int(input('Entre com o Segundo Bimestre: '))
if b > 10:
    b = int(input('Você digitou errado. Segundo Bimestre: ' ))
c = int(input('Entre com o Trimestre Bimestre: '))
if c > 10:
    c = int(input('Você digitou errado. Terceiro Bimestre: ' ))
d = int(input('Entre com o Quarto Bimestre: '))
if d > 10:
    d = int(input('Você digitou errado. Quarto Bimestre: ' ))
media = (a + b + c + d) / 4
if a <= 10 and b<=10 and c<=10 and d <=10:
    print('A Media é:{}'.format(media))
else:
    print('Foi informado alguma nota errada: ')



# VERIFICANDO MEDIA ENTRE 4 NUMEROS DIGITADOS
# a = int(input('Entre com o Primeiro Bimestre: '))
# b = int(input('Entre com o Segundo Bimestre: '))
# c = int(input('Entre com o Trimestre Bimestre: '))
# d = int(input('Entre com o Quarto Bimestre: '))
# media = (a + b + c + d) / 4
# if a <= 10 and b<=10 and c<=10 and d <=10:
#     print('A Media é:{}'.format(media))
# else:
#     print('Foi informado alguma nota errada: ')


# VERIFICANDO SE um entre dois NUMEROS DIGITADOS É PAR
# a = int(input('Entre com o Primeiro Valor: '))
# b = int(input('Entre com o Segundo Valor: '))
# resto_a = a % 2
# resto_b = b % 2
# #if resto_a == 0 or resto_b == 0:
# if resto_a == 0 or not resto_b >0:
#      print('Foi dado um Número Par ')
# else:
#      print('Nenhum Número digitado é Par')



# VERIFICANDO SE O NUMERO DIGITADO É PAR
# a = int(input('Entre com um Valor: '))
# resto = a % 2
# if resto == 0:
#     print('Número é Par ')
# else:
#     print('Número é Impar')

# a = int(input('Entre com o primeiro Valor:'))
# b = int(input('Entre com o segundo Valor:'))
# c = int(input('Entre com o terciro Valor:'))
#
# if a > b and a > c:
#     print('o maior numero é:{}'.format(a))
# elif b > a and b > c:
#     print('o maior numero é:{}'.format(b))
# else:
#     print('o maior numero é:{}'.format(c))
# print('final do programa')