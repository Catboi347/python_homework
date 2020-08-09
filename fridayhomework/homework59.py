employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}
new_dict = dict.fromkeys(employees, defaults)
print (new_dict)