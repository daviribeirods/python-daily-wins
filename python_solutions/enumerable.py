from typing import Iterable, Callable

def one(array: Iterable, fun: Callable) -> bool:
    i = 0
    for num in array:
        i+= 1 if fun(num) else 0
        if i > 1:
            return False
    return True if i==1 else False

equals_9 = lambda x: x == 9
less_than_9 = lambda x: x < 9
greater_than_9 = lambda x: x > 9

# print(one([6, 7, 8, 9, 10, 11], less_than_9))

# best and elegant solution
# def one(array, fun):
    # return sum(map(fun, array))==1

#array = [6, 7, 8, 9, 10, 11]
#fun = lambda x: x==9

#print(one(array, fun))

# A melhor solução ou melhor prática usou o map.
# Essa função aplica a função passada por parâmetro para
# todos os outros valores da lista ou iterável. Pode-se usar mais
# de uma lista, contanto que exista na função um parâmetro para cada
# (ex: 2 listas, função com 2 parametros, e assim por diante).
# Depois, como o problema é contar 1, soma-se os True e False (True == 1)
# e se for igual a 1, funfo