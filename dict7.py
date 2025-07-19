from randomusers import randomuser_data
ages=list(map(lambda n:n['dob']['age'],randomuser_data['results']))
average=float(sum(ages)/len(ages))
print(average)