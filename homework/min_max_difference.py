from random import randint


def max_min_elem(l1):
    temp_max = l1[0]
    temp_min = l1[0]
    for i in range(1, len(l1)):
        if temp_max < l1[i]:
            temp_max = l1[i]
        if temp_min > l1[i]:
            temp_min = l1[i]
    return temp_min, temp_max


def create_random_list(n=None, range_min=None, range_max=None):
    if n is None:
        n = 30
    if range_min is None:
        range_min = 0
    if range_max is None:
        range_max = 99
    return [randint(range_min, range_max) for p in range(0, n)]


def problem_min_max_difference(n=None, range_min=None, range_max=None):
    if n is None:
        n = 30
    if range_min is None:
        range_min = 0
    if range_max is None:
        range_max = 99
    min_elem, max_elem = max_min_elem(create_random_list(n=n, range_min=range_min, range_max=range_max))
    return max_elem - min_elem

print(problem_min_max_difference())