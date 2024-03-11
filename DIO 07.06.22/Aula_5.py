#Criação de Listas
lista = [12, 10, 7, 5]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'Arara']
#print(lista)
#print(lista_animal[1])

# for x in lista_animal:
#     print(x)

#aqui printa todos os numeros e a soma no final
# soma = 0
# for x in lista:
#     print(x)
#     soma+= x
# print(soma)

#aqui soma toda a lista e apresenta o resultado
# print(sum(lista))

#aqui apresenta o maior e o menor valor dentro de uma lista, se for texto
#vai verificar qual letra vem primeiro
# print(max(lista))
# print(min(lista))
# print(max(lista_animal))
# print(min(lista_animal))

#aqui procurando uma intem na lista
# if 'lobo' in lista_animal:
#     print('existe um lobo na lista ?')
# else:
#     print('não existe lobo na lista')

#Multiplicando uma lista
# nova_lista = lista_animal * 3
# print(nova_lista)

#incluindo lobo na nova lista, e comando pop() retira o ultimo intem da lista
#ou se indicar o item (1) remove item diretamente e o remove. se vc ja conhecer diretamente o item

# if 'lobo' in lista_animal:
#     print('existe um lobo na lista ?')
# else:
#     print('não existe lobo na lista. Será incluido na lista.')
#     lista_animal.append('lobo')
#     print(lista_animal)

# lista_animal.pop()
# print(lista_animal)

# lista_animal.remove('elefante')
# print(lista_animal)

#aqui ordenando os valores das listas
# lista.sort()
# lista_animal.sort()
# print(lista)
# print(lista_animal)
# lista_animal.reverse()
# print(lista_animal)

#Diferença Tupla x Lista , lista é mutavel, e tupla é imutavel, não da para alterar
# lista_animal[0] = 'macaco'
# print(lista_animal)

#para forma uma tupla basta usar os valores entre parentesis ()
lista_animal[0] = 'macaco'
tupla = (1, 10, 12, 14)
# print(tupla)
# print(tupla[2])
#comando len. me retorna quantos elementos tem na lista
print(len(tupla))
print(len(lista_animal))
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list(tupla)
print(type(lista_numerica))
lista_numerica[0] = 100
print(lista_numerica)





