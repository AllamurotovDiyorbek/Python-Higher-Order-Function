from randomusers import randomuser_data
mail=list(map(lambda n:n['email'],randomuser_data['results']))
result=list(filter(lambda n:n.startswith("g"),mail))
print(result)