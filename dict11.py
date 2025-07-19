from randomusers import randomuser_data
result=list(filter(lambda n:n['location']['timezone']['offset']=='+5:30',randomuser_data['results']))
print(f"{result['name']['first']} {result['name']['first']}"+result['location']['city'])