def value_chain(*args):
    for value in args:
        if isinstance(value, (str, bytes)):
            yield value
            continue
        try:
            yield from value
        except TypeError:
            yield value    