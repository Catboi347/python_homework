result_string=""
for row in range(0,7):
    for column in range(0,7):
        if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):
            result_string = result_string +"*"
        else:
            result_string=result_string+ " "
    result_string=result_string + "\n" 
print(result_string)
