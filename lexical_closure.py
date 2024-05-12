#lexical closure

def Person(age, name):
    def adult():
        return f"{name} is Adult"
    def kid():
        return f"{name} is Kid"
    
    
    if age > 18:
        return adult
    else:
        return kid
    

print(Person(20,"ali")())   