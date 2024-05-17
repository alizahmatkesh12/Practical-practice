from itertools import chain, repeat, islice

def take(iterable, n):
    return list(islice(iterable, n))

def repeat_each(itreable, n = 2):
    return chain.from_iterable(map(repeat, itreable, repeat(n)))
