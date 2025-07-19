text = ["apple", "34", "banana", "100", "abc", "75"]
def numbeer(text:list)->list:
    c=0
    p=[]
    for item in text:
        for son in item:
            if 47<ord(son)<58:
                pass
            else:
                c+=1
            if c==0:
                return True
s=list(filter(lambda n:n.isdigit() , text))
print((s))