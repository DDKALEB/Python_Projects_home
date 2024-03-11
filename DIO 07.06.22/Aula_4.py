# VERIFICANDO MEDIA ENTRE 4 NUMEROS DIGITADOS
a = int(input('Entre com o Primeiro Bimestre: '))
while a > 10:
    a = int(input('Você digitou errado. Primeiro Bimestre: ' ))
b = int(input('Entre com o Segundo Bimestre: '))
while b > 10:
    b = int(input('Você digitou errado. Segundo Bimestre: ' ))
c = int(input('Entre com o Trimestre Bimestre: '))
while c > 10:
    c = int(input('Você digitou errado. Terceiro Bimestre: ' ))
d = int(input('Entre com o Quarto Bimestre: '))
while d > 10:
    d = int(input('Você digitou errado. Quarto Bimestre: ' ))
media = (a + b + c + d) / 4
if a <= 10 and b<=10 and c<=10 and d <=10:
    print('A Media é:{}'.format(media))
else:
    print('Foi informado alguma nota errada: ')





# #Fazer uma repetição ate que uma condição seja verdadeira.
# nota = int(input('Entre com a nota: '))
# while nota > 10:
#     nota = int(input('Nota invalida, Entre com a nota correta: '))
# print(nota)

# a = 0
# while a <= 10:
#     print(a)
#     a += 1


# #Verificando Todos os Numeros primos 1 a X, sendo que X é informado pelo Usuario.
# a = int(input('Entre com um Valor: '))
# for num in range(a+1):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         #print(x, resto)
#         if resto == 0:
#            div += 1
#
#     if div == 2:
#         print(num)

# #Verificando Todos os Numeros primos 1 a 100.
# for num in range(101):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         #print(x, resto)
#         if resto == 0:
#            div += 1
#
#     if div == 2:
#         print(num)


#Verificando se um Numero é Numero Primo.
# a = int(input('Entre com o Número: '))
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#        div += 1
#
# if div == 2:
#     print('Número {} é Primo' .format(a))
# else:
#     print('Número {} não é Primo' .format(a))


# #Verificando se um Numero é Numero Primo.
# a = int(input('Entre com o Número: '))
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#        div = div +1
#
# if div == 2:
#     print('Número {} é Primo' .format(a))
# else:
#     print('Número {} não é Primo' .format(a))


# a = int(input('Entre com o Número: '))
# for x in range(1, a + 1):
#     resto = a % x
#     print(resto)





#Printa um numero de x a y, ou 1 a 100, etc
# for x in range(100):
#     print(x)
# for x in range(2, 110):
#    print(x)
# for x in range(1, 100):
#     print(x)

# Um número é classificado como primo se ele é maior do que um e é divisível apenas por um e por ele mesmo.
# Apenas números naturais são classificados como primos. Antes de saber mais sobre o número primo, é importante relembrar algumas regras de divisibilidade,
# que ajudam na identificação de quais números não são primos.
# Divisibilidade por 2: todo número par é divisível por 2. Os números pares são aqueles terminados em 0, 2, 4, 6 e 8.
# Divisibilidade por 3: um número é divisível por 3 se a soma dos seus algarismos der um número divisível por 3.
# Divisibilidade por 4: um número é divisível por 4 se ele for divisível duas vezes por 2 ou, então, se seus dois últimos algarismos forem divisíveis por 4.
# Divisibilidade por 5: todo número terminado em 0 ou 5 é divisível por cinco.
# Divisibilidade por 6: se um número for par e também divisível por 3, será divisível por 6.
# Divisibilidade por 7: um número é divisível por 7 se a diferença entre o dobro do último algarismo e o restante do número resultar em um número múltiplo de 7.
# Essas são as principais regras de divisibilidade. Para encontrar cada número primo menor do que 100, utilizamos o “Crivo de Eratóstenes”.
# Na tabela a seguir, iremos cancelar os números que não são primos seguindo esta ordem:
# O número 1 estará fora, pois, pela condição inicial, os números primos são maiores que um (será destacado de preto);
# Não pare agora... Tem mais depois da publicidade ;)
# Os números terminados em 0, 2, 4, 6 e 8 estarão fora porque são divisíveis por dois (serão destacados vermelho);
# Os números terminados em 5 estarão fora porque são divisíveis por 5 (serão destacados de azul). Os números terminados em zero já foram cortados;
# Os números cuja soma dos algarismos for 3 estarão fora por serem divisíveis por três (serão destacados de laranja);
# Os números que são divisíveis por 7 serão retirados também (serão destacados de verde)
#
#
# Os números destacados em amarelo são aqueles que só são divisíveis por 1 e por eles mesmos, isto é, não obedecem a nenhum dos critérios de divisibilidade que comentamos acima.
# Portanto, pelo “Crivo de Eratóstenes”, os números 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,53, 59, 61, 67, 71, 73, 79, 83, 89 e 97 são os únicos números primos menores que 100.
#
# Na imagem inicial do texto, há vários números primos entre 100 e 1000. Hoje já se conhece uma grande quantidade de números primos,
# mas não se sabe qual é o maior número primo existente. Esse é um dos grandes enigmas matemáticos que farão rico o seu desvendador.
# Há um prêmio milionário para aquele que descobrir o maior dos números primos...
