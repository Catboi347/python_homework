row_list = int(input("Type in the amount of rows you want"))
columns_list = int(input("Type in the amount of columns you want"))
combine_list = [[y for y in range(columns_list)]for x in range(row_list)]
for x in range(row_list):
    for y in range(columns_list):
        combine_list[x][y] = x*y
print (combine_list)