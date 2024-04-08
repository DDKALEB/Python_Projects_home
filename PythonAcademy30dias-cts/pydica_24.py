# -*- coding: utf-8 -*-
"""PyDica#24.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14d0K5ki3c7eInn6iX9mklKVzGtjwCKit

# PyDica #24 | Os tais @staticmethod e @classmethod
"""

# Salve salve Pythonista 👋
# Ao trabalhar com classes em Python, você pode já ter se deparado (ou ainda vai) com os decoradores @staticmethod e @classmethod.
# Mas qual é a real diferença entre eles e quando usá-los?

# Vamos esclarecer isso na PyDica de hoje!

# Exemplo 1: Usando @staticmethod

class Classe:
  @staticmethod
  def metodo_static(x, y):
    return x + y

# Chamada sem instanciar a classe
resultado = Classe.metodo_static(3, 4)

print(resultado)
# A saída será: 7

## @staticmethod é basicamente uma função regular, mas que pertence à classe,
# e não usa nem a instância (self) nem a classe (cls) em sua definição.

# Exemplo 2: Usando @classmethod

class Pizza:
  pedaços = 8

  @classmethod
  def mudar_quantidade(cls, qtde):
      cls.pedaços = qtde

Pizza.mudar_quantidade(12)

print(Pizza.pedaços)
# A saída será 12

## @classmethod trabalha com a classe e não com a instância. Ele recebe o primeiro parâmetro como a classe, geralmente nomeado como cls.

#Então, quando usar cada um?

# @staticmethod: Quando você precisa de uma função que não acessa nenhum atributo da classe/instância, mas faz sentido mantê-la dentro da classe por questões de organização.
# @classmethod: Quando você precisa de uma função que opera em atributos da classe e não específicos da instância.

"""Espero que essa dica tenha esclarecido a diferença entre esses dois decoradores. Eles são bem úteis quando usados corretamente!



Conhecer, estudar e aplicar os conceitos da Programação Orientada a Objetos é de extrema importância para um Pythonista profissional!



E é por isso que na Jornada Python, você vai ter um módulo inteiro apenas sobre Programação Orientada a Objetos, olha só isso:


Portanto não perca tempo e entre para a Jornada agora mesmo clicando no botão abaixo!



E não se esqueça de usar o seu cupom exclusivo PYDICA20 para garantir o desconto especial dos leitorer das PyDicas!
"""





