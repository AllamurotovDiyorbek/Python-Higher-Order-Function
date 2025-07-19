people = [
  {"name": "Ali", "age": 25},
  {"name": "Sami", "age": 99},
  {"name": "Lola", "age": 31}
]
oldest = max(people, key=lambda x: x["age"])
print(oldest["name"], oldest["age"])
