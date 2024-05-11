import random


class OneTime():

    def encrypt(self, text):
        plain = (ord(x) for x in text)
        key = []
        chiper = []
        
        for i in plain:
            k = random.randint(1, 300)
            c = (i + k) * k
            chiper.append(c)
            key.append(k)
        return  chiper, key  
    
    
    def decrypt(self, chiper, key):
        plain = []
        
        for i in range(len(key)):
            p = int((chiper[i] - key[i] ** 2 ) / key[i])
            plain.append(chr(p))
        result = ''.join(i for i in plain)
        return result   
    
    
    
c, k = OneTime().encrypt("ali")
print(c)
print(k)

print(OneTime().decrypt(c, k))