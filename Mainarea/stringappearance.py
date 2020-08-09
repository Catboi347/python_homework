def count_string(statement):
    print("Given String: ", statement)
    count = 0
    for i in range(len(statement) - 1):
        count += statement[i: i + 6] == 'Danyal'
    return count

count = count_string("Danyal loves cats. Danyal loves to play videogames. How many times has Danyal apperared in the string?")
print("Danyal appeared", count, "times")
if count == 3:
    print (" You got it right!")
else:
    print ("You got it wrong")