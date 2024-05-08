




def is_isomorphic(str1,str2):
    if len(str1) != len(str2):
        return False
    
    dict = {}
    set_values = set()
    
    for i in range(len(str1)):
        if str1 not in dict:
            dict[str1[i]] = str2[i]
            set_values.add(str2[i])
        
    return dict, set_values

print( is_isomorphic('foo', 'bar'))    
        
        