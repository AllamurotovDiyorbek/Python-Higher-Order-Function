from randomusers import randomuser_data
result=list(
    map(
    lambda user:user['name']['first']+" "+user['name']['last'],
    randomuser_data['results']
    )
)
print(result)