def double_letters(word):
    double_list = []
    for i in word:
        double_list.append(i)
        for x in double_list:
            if double_list.index(x) == double_list.index(x)+1:
                double_checker = True
            else:
                double_checker = False
    return double_checker

print (double_letters("letter")) 
