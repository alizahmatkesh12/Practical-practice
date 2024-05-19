def always_iterable(obj, base_tpye=(str, bytes)):
    if obj is None:
        return iter(())
    
    if(base_tpye is not None) and isinstance(obj, base_tpye):
        return iter((obj,))
    
    try:
        return iter(obj)
    except TypeError:
        return iter((obj, ))