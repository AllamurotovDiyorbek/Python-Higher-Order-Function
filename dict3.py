from randomusers import randomuser_data
male_count=len(list(filter(lambda user:user['gender'] == 'male',randomuser_data['results'])))
female_count=len(list(filter(lambda user:user['gender'] == 'female',randomuser_data['results'])))
print(f"male : {male_count}, 'female : '{female_count}")