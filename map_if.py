def map_if(iterable, pred, func, func_else = lambda x: x):
    for item in iterable:
        yield func(item) if pred(item) else func_else(item)
        
        