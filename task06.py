emails = ["ali@gmail.com", "vali@yahoo.com", "sami@gmail.com", "bek@outlook.com"]
results = list(filter(lambda email: email.endswith("@gmail.com"), emails))
print(results)