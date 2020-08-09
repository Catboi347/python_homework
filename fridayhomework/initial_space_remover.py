import csv
with open("csv_list.csv", "r") as f:
   data = csv.reader(f, skipinitialspace=False)
   for row in data:
     print(", ".join(row))
with open("csv_list.csv", "r") as f:
   data = csv.reader(f, skipinitialspace=True)
   for row in data:
     print(", ".join(row))