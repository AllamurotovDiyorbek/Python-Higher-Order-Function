votes = [
  {"option": "A", "votes": 123},
  {"option": "B", "votes": 145},
  {"option": "C", "votes": 97}
]
a=votes[0]
d=max(votes,key=lambda a:a['votes'])
print(d)