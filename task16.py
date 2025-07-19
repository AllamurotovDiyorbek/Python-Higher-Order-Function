data = [123, "apple", "banana", "cat", 456, "mango", "elephant"]
rs=filter(
    lambda n:type(n)==str and len(str(n)) >5,
    data
)
print(list(rs))