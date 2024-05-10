# amir => [1, 13, 25, 23]

def encode(s):
    
    return[ord(i) for i in s]

def decode(decode):
    
    return "".join((chr(i) for i in decode))


print(encode("ali"))
print(decode([97, 108, 105]))

