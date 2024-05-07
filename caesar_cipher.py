from string import ascii_letters

def encrypt(abs:str, key:int) -> str:
    alpha = ascii_letters    
    result = ''
    
    for i in abs:
        if i not in alpha:
            result += i
        else:
            new_key = alpha.index(i) + key            
            result += alpha[new_key]
            
    return(result)


def decrypt(abs:str, key:int) -> str:
    key *= -1
    return encrypt(abs, key)


def brute_force(abs: str) -> dict:
    alpha = ascii_letters
    key = 1
    result = ''
    burte_force_data = {}
    
    while key <= len(alpha):
        result = decrypt(abs, key)
        burte_force_data[key] = result
        result = ''
        key += 1
        
    return(burte_force_data)           
    
    
print(sorted(brute_force("Alislm1241").items(),reverse=True))