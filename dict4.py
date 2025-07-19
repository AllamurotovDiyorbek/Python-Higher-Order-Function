from randomusers import randomuser_data
result=list(filter(lambda n:n['registered']['age']<90,randomuser_data["results"]))
email=list(map(lambda n:n['email'],result))
print(email)