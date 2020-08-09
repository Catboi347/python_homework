import random
def random_number():
    random_list = []
    for i in range(1,101):
        random_list.append(i)
        weird_number = random.choice(random_list)
    return weird_number

print (random_number())