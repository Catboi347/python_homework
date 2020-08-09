import csv
with open("csv_list.csv", newline="") as f:
   reader = csv.reader(f)
   data_list = list(reader)
print(data_list)