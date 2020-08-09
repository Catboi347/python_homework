import csv
import sys
with open('csv_list.csv', 'wt') as f:
    writer = csv.writer(f)
    writer.writerow(('id1', 'id2', 'date'))
    for i in range(3):
        row = (i + 1,chr(ord('a') + i),'7/{:02d}/2020'.format(i + 1))
        writer.writerow(row)
print(open('csv_list.csv', 'rt').read())