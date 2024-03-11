#Set = conjunto, em conjunto só pode ter um elemento do mesmo tipo, se tiver repitido ele ignora
# conjunto = {1, 2, 3, 4, 4, 2}
# conjunto.add(5)
# conjunto.discard(2)
# print(type(conjunto))
# print(conjunto)

conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conunto_uniao = conjunto.union(conjunto2)
print('União: {}'.format(conunto_uniao))
#temos aqui a união dos conjuntos
conjunto_interseccao = conjunto.intersection(conjunto2)
print('Intersecção: {}'.format(conjunto_interseccao))
conjunto_diferenca1 = conjunto.difference(conjunto2)
#imprimi só os numeros que tem no conjunto1
conjunto_diferenca2 = conjunto2.difference(conjunto)
#imprimi só os numeros que tem no conjunto2
print('Diferença entre 1 e 2: {}'.format(conjunto_diferenca1))
print('Diferença entre 2 e 1: {}'.format(conjunto_diferenca2))
#diferença simetrica
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferença Simetrica: {}'.format(conjunto_diff_simetrica))
#pertinencia subconjunto

# conjunto_a = {1, 2, 3}
# conjunto_b = {1, 2, 3, 4, 5}
# conjunto_subset = conjunto_b.issubset(conjunto_a)
# print(conjunto_subset)
# conjunto_superset = conjunto_b.issuperset(conjunto_a)
# print(conjunto_superset)

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('A é Subconjunto de B: {}'.format(conjunto_subset))
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B é um Superconjunto A: {}'.format(conjunto_superset))

lista = ['cachorro', 'cachorro', 'gato', 'gato', 'Elefante']
print(lista)
conjunto_animais = set(lista)
#converte para conjunto
print(conjunto_animais)
lista_animais = list(conjunto_animais)
print(lista_animais)
