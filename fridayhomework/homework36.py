def showEmployee(name, salary=9000):
    print ("The employee", name +"'s salary is :","$"+ str(salary))
name = input("Type in your name ")
salary = int(input("Type in your salary "))
showEmployee(name, salary)
showEmployee(name) 
