month = input("Input the month (e.g. January, February etc.):")                     
day = int(input("Input the day:"))
if month in ("January", "February", "March"):
    season = "winter"
elif month in ("April", "May", "June"):
    season = "spring"
elif month in ("July", "August", "September"):
    season = "summer"
else:
    season = "fall"
if (month == "march") and (day > 19):
    season = "spring"
elif (month == "June") and (day > 20):
    season = "summer"
elif (month == "September") and (day > 21):
    season = "fall"
elif (month == "december") and (day > 20):
    season = "winter"
print (season)
    
