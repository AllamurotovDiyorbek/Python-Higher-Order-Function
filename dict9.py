from randomusers import randomuser_data
result=list(map(
    lambda n:
        (
        str(n['location']['coordinates']['latitude']),
        str(n['location']['coordinates']['longitude'])
        ),
        randomuser_data['results']))
print(result)