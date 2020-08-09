import re
password = input("Input a password ")
password_check = 0
while True:
    if len(password) > 9:
        password_check = -1
        break
    elif not re.search("[a-z]", password):
        password_check = -1
        break
    elif not re.search("[A-Z]", password):
        password_check = -1
        break
    elif not re.search("[0-9]", password):
        password_check = -1
        break
    elif not re.search("[_@$]", password):
        password_check = -1
        break
    elif re.search("/s", password):
        password_check = -1
        break
    else:
        password_check = 0
        print ("Valid Password")
        break

if password_check == -1:
    print ("Invalid Password")
    


