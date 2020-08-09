f = open("C:\PythonProjects\data_files\multiply.txt", "r")
def multiply(_list):
    one = f.readline()
    product = int(one)
    for i in _list:
        product *= i
    return product
print (multiply([8,2,3,-1,7]))
