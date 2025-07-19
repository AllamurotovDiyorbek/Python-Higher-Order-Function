sentence = "Functional programming in Python is very powerful and elegant"
lst=sentence.split()
result=sorted(lst,key=lambda n:len(n),reverse=True)
print(result[:3])