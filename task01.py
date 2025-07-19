numbers = [4, -2, 0, 7, -9, 3, -1, 5]
result=filter(
    lambda n:n>0,
    numbers
)
print(list(result))