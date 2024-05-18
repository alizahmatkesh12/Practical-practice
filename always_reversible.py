def always_reversible(iterable):
    try:
        return reversed(always_reversible)
    except TypeError:
        return reversed(list(iterable))
