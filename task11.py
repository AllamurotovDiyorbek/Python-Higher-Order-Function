nums = list(range(1, 21))
rs=filter(
    lambda n:n%2==0,
    nums
)
rs=map(
    lambda n :n**2,
    list(rs)
)
print(list(rs))
