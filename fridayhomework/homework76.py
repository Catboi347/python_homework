months = input("Input a month")
if (months == "february"):
    print (months, "= 28/29 days")
elif (months == "april") or (months == "june") or (months == "september") or (months == "november"): 
    print (months, "= 30 days")
else:
    print (months, "= 31 days")