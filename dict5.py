from randomusers import randomuser_data
sort=list(sorted(randomuser_data['results'],key=lambda n:n['dob']['age'],reverse=True))
lst=[]
for i in sort:
    lst.append({"name":f"{i['name']['first']} {i['name']['last']}"})
    lst.append({"age":i['dob']['age']})
print(lst)