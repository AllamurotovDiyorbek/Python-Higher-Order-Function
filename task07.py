prices = ["$120", "$340", "$50", "$90"]
results=map(
    lambda son:float(son.replace("$","")),
    prices
)
print(list(results))