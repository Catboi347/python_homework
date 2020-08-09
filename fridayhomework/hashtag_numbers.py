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
}
def seven_segment(number):
    digits = [representations[digit] for digit in number]
    print (digits)
    for i in range(5):
        print("  ".join(segment[i] for segment in digits))
number = input("Input a number ")
print (seven_segment(number))
