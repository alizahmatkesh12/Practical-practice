def only(iterable, defualt=None, too_long=None):
    it = iter(iterable)
    first_value = next(it, defualt)
    
    try:
        second_value = next(it)
    except StopIteration:
        pass
    else:
        msg = (
            "Expected exactly one item in iterable, but got {}, {}, "
            "and perhaps more".format(first_value, second_value)
        
        )
        raise too_long or ValueError(msg)
    return first_value     