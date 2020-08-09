import csv
reader = csv.DictReader(open("csv_list.csv"))   
for row in reader:
    print(row)