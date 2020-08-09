import csv
with open("csv_list.csv", newline="") as f:
 data = csv.reader(f, delimiter=" ", quotechar="|")
 for row in data:
   print(", ".join(row))