def mid(string):
    mid_letter = ""
    if len(string)//2==0:
        mid_letter =  ""
    else:
        mid_letter = string[(len(string)-1)//2:(len(string)+2)//2]
    return mid_letter

print (mid("abc"))
        