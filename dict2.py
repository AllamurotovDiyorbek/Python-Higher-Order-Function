from randomusers import randomuser_data
result=list(filter(lambda n:n['location']['country']=='India',randomuser_data['results']))
p=[]
for i in result:
    p.append({'name': f"{i['name']['first']} {i['name']['last']}",'email':i['email']})
print(p,)