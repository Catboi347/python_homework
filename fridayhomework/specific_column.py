import csv
with open('csv_list.csv', newline='') as csvfile:
    data = csv.DictReader(csvfile)
    print("Rank Country")
    for row in data:
        print(row["Rank"], row["Country"])