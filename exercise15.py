def up_down(number):
    up_down_list = []
    up_num = number+1
    down_num = number-1
    up_down_list.append(down_num)
    up_down_list.append(up_num)
    return tuple(up_down_list)

print (up_down(12))