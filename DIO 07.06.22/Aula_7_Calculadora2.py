#Metodo e Função
#função é tudo que retorna um valor,metodo não
class calculadora:
    def __init__(self):
        pass
    def soma(self, valor_a, valor_b):
        return valor_a + valor_b
    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b
    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b
    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b
# print(soma(1, 2))
# print(soma(3, 4))
# print(subtracao(10, 2))
# print(multiplicacao(10, 2))
# print(divisao(10,2))


#estanciar uma classe

calculadora = calculadora()

print(calculadora.soma(10, 2))
print(calculadora.subtracao(5, 3))
print(calculadora.divisao(1, 2))
print(calculadora.multiplicacao(10, 5))
