#Metodo e Função
#função é tudo que retorna um valor,metodo não
class calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2
    def soma(self):
        return self.valor_a + self.valor_b
    def subtracao(self):
        return self.valor_a - self.valor_b
    def multiplicacao(self):
        return self.valor_a * self.valor_b
    def divisao(self):
        return self.valor_a / self.valor_b
# print(soma(1, 2))
# print(soma(3, 4))
# print(subtracao(10, 2))
# print(multiplicacao(10, 2))
# print(divisao(10,2))


#estanciar uma classe

calculadora = calculadora(10, 2)
print(calculadora.valor_a)
print(calculadora.soma())
print(calculadora.subtracao())
print(calculadora.divisao())
print(calculadora.multiplicacao())

