from randomusers import randomuser_data
from collections import Counter
def group_users_by_nationality(data):
    nationalities = list(map(lambda user: user['nat'], data['results']))
    return dict(Counter(nationalities))
print(group_users_by_nationality(randomuser_data))  