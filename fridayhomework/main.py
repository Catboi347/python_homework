representations = {
    '0': ('###', '# #', '# #', '# #', '###'),
    '1': ('## ', ' # ', ' # ', ' # ', '###'),
    '2': ('###', '  #', '###', '#  ', '###'),
    '3': ('###', '  #', '###', '  #', '###'),
    '4': ('# #', '# #', '###', '  #', '  #'),
    '5': ('###', '#  ', '###', '  #', '###'),
    '6': ('###', '#  ', '###', '# #', '###'),
    '7': ('###', '  #', '  #', '  #', '  #'),
    '8': ('###', '# #', '###', '# #', '###'),
    '9': ('###', '# #', '###', '  #', '###'),
    '.': ('   ', '   ', '   ', '   ', ' # '),    
    'A': ('  #  ', '  #  ', '#####', '  #  ', '  #  '),
    'S': ('     ', '     ', '#####', '     ', '     '),
    'M': ('#   #', ' # # ', '  #  ', ' # # ', '#   #'),
    'D': ('  #  ', '     ', '#####', '     ', '  #  '),
    'E': (' ##  ', '     ', '     ', '     ', '     '),
    'Q': ('     ', '#####', '     ', '#####', '     ')
}
csd = 0
Eq = "Q"   
print ("Type M for multiplication")
print ("Type A for addition")
print ("Type S for subtraction")
print ("Type D for division")
print ("Type E for the exponents")
ops = input("Please type in your choice ")
number1 = int(input("Provide us with the 1st  number "))
def multiply(number1, number2):
    return number1*number2

def add(number1, number2):
    return number1+number2

def subtract(number1, number2):
    return number1-number2

def divide(number1, number2):
    return number1 / number2

def power(number1, number2):
    return number1 ** number2


number2 = int(input("Provide us with the 2nd number "))
if ops == "M":
    csd = multiply(number1, number2)
if ops == "A":
    csd = add(number1, number2)
if ops == "S":
    csd = subtract(number1, number2)
if ops == "D":
    csd = divide(number1, number2)
if ops == "E":
    csd = power(number1, number2)
cmd = str(number1) + ops + str(number2) + Eq + str(csd)
def seven_segment(number):
    digits = [representations[digit] for digit in number]
    for i in range(5):
        print("  ".join(segment[i] for segment in digits))
print (seven_segment(cmd))