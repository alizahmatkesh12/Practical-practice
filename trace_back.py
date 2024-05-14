_marker = object()

def first(itreable, defualt = _marker):
    try:
        return next(iter(itreable))
    except StopIteration as e:
        if defualt is _marker:
            raise ValueError("first() was called on an empty iterable, and no "
                             "defualt value was provided. ") from e
            
            
        return defualt
    
    












 