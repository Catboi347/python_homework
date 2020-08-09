rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
sampleDict ={'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
for item in rollNumber:
    found = False
    for keyvalue in sampleDict.values():
        if item == keyvalue:
            found = True
            break
    if found == False:
        rollNumber.remove(item)
print ("after removing unwanted elements from list ", rollNumber)