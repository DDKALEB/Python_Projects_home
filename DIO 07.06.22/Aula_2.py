# a = 10
# b = 5
a = int(input('Entre com o primeiro Valor:'))
b = int(input('Entre com o primeiro Valor:'))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
print(type(soma))
soma = str(soma)
# print('soma: '+ str(soma))
# print('soma: {}. subtracao: {}'.format(soma,subtracao))
print('soma: {soma}. \nsubtracao: {sub}.'
      '\nmultiplicacao:{multiplicacao}'
      '\ndivisao:{divisao}'
      '\nresto:{resto}'.format(soma=soma,
                                                sub=subtracao, multiplicacao=multiplicacao, divisao=divisao, resto=resto))
# Tem de ser na sequencia (acima) correta
# print(subtracao)
# print('subtracao: '+ str(subtracao))
# print(multiplicacao)
# print(int(divisao))
# print(type(divisao))
# print(resto)
# # x = '1'
# soma2 = int(x) + 1
# print(soma2)
