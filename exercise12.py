def div_3(single_num):
    div_checker = True
    if single_num % 3 == 0:
        div_checker = True
    else:
        div_checker = False

    return div_checker

print (div_3(6))
