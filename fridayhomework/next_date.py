import datetime
year = int(input("Input a year:"))
month = int(input("Input a month [1-12]:"))
date = int(input("Input a day [1-31]"))
x = datetime.datetime(year, month, date)
end_date = x + datetime.timedelta(days=1)
print(end_date) 