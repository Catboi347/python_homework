def capital_indexes(z):
    capital_list = []
    for i, x in enumerate(z):
        if x.isupper():
            capital_list.append(i)
    return capital_list
print(capital_indexes("HeLlO"))