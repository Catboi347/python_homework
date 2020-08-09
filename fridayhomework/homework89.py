from datetime import datetime
time_in_string = "21-5-2020 17:54:11"
time_in_datetime = datetime.strptime(time_in_string, "%d-%m-%Y %H:%M:%S")
print (time_in_datetime)
now = time_in_datetime
year = lambda a: a.year
month = lambda a: a.month
day = lambda a: a.day
time = lambda a: a.time()
print (year(now))
print (month(now))
print (day(now))
print (time(now))
