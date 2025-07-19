from randomusers import randomuser_data
result=filter(lambda n:n['registered']['date'],randomuser_data['results'])
print(result['registered'])