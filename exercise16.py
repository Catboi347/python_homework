def triple_and(bool1, bool2, bool3):
    bool_determiner = True
    if bool1 and bool2 and bool3 == True:
        bool_determiner = True
    else:
        bool_determiner = False
    return bool_determiner

a = 1
b = 2

print (triple_and(a==b,a=b,a<b))
print (triple_and(a<b,a=b,a==b))