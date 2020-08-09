f = open("C:\PythonProjects\data_files\plus.txt", "r")
def addition(_list):
    zero = f.readline()
    _sum = int(zero)
    for i in _list:
        _sum += i
    return _sum
print (addition([8,2,3,0,7]))
