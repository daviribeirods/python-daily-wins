# https://www.codewars.com/kata/5704bf9b38428f1446000a9d
from math import ceil
def histogram(array: list, bin_width: int) -> list:

    if len(array) == 0:
        return []

    histogram_array_length = max(array) + 3 if bin_width % 2 == 0 else max(array) + 2
    final_histogram = []
    aux = -1

    for i in range(bin_width, histogram_array_length, bin_width):
        func_test = lambda x: aux < x < i
        final_histogram += [(sum(map(func_test, array)))]
        aux += bin_width

    return final_histogram

# Resposta correta não otimizada:
# Meu erro tava sendo arredondar pra cima, ao invés de arredondar pra baixo.
# Poderia ter usado o math.floor ou apenas o divisor de inteiros //
def histogram_2(array: list, bin_width: int) -> list:

    if len(array) == 0:
        return []
    
    max_value = max(array)
    number_bins = max_value // bin_width
    histogram_list = []
    bin_min = -1
    bin_max = bin_width

    for i in range(0,number_bins + 1):
        func_aux = lambda x: bin_min < x < bin_max
        histogram_list += [sum(map(func_aux, array))]

        bin_min += bin_width
        bin_max += bin_width

    return histogram_list


print(histogram_2([1, 1, 0, 1, 3, 2, 6], 2))

array = [7]
array_max_value = max(array)
bin_width = 3

print(f'{array_max_value} divided by {bin_width} = {ceil(array_max_value / bin_width)} rest {array_max_value % bin_width}')