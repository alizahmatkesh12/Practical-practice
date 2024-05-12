# nested functions

def Person(age):
    def adult(name):
        return f"{name} is Adult "
    def kid(name):
        return f"{name} is Kid "
    
    
    if age > 18:
        return adult
    else:
        return kid
    
    
p1 = Person(20)

print(p1("ali"))


 