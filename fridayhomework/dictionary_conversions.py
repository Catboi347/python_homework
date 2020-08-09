speed ={'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
updated_list = []
for x in speed.values():
    count = updated_list.count(x)
    if count == 0:
        updated_list.append(x)
print (updated_list)        