from randomusers import randomuser_data
result=max(randomuser_data['results'],key=lambda n:n['dob']['age'])
print(f" Name : {result['name']['first']} {result['name']['last']}, age :{result['dob']['age']} email : {result['email']}")