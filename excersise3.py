def online_count(dictionary):
    counter = 0
    for i in dictionary:
        x = dictionary[i]
        if x == "online":
            counter +=1
    return counter

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
print (online_count(statuses))