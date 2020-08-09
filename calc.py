from flask import Flask, flash, redirect, render_template, request, session, abort
from app import app
import random

app = Flask(__name__)

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
    'Addition': ('  #  ', '  #  ', '#####', '  #  ', '  #  '),
    'Subtraction': ('     ', '     ', '#####', '     ', '     '),
    'Multiplication': ('#   #', ' # # ', '  #  ', ' # # ', '#   #'),
    'D': ('  #  ', '     ', '#####', '     ', '  #  '),
    'Q': ('     ', '#####', '     ', '#####', '     ')
}

solution = 0
list1 = []
list2 = []

for i in range (1, 101):
    list1.append(i)
    bar = random.choice(list1)
for x in range (1, 101):
    list2.append(x)
    bar2 = random.choice(list2)

operator_list = ["Addition", "Subtraction", "Multiplication", "Division"]
operator = random.choice(operator_list)

if operator == "Addition":
    solution = bar + bar2

if operator == "Subtraction":
    solution = bar - bar2

if operator == "Multiplication":
    solution = bar * bar2

if operator == "Division":
    solution = bar / bar2

@app.route('/')
@app.route('/calc')
def calc():
    return render_template('calc.html', title='Calculator', foo=bar, foos=bar2, operator=operator, answer=solution)

@app.route("/add/<number1>/<number2>/")
def add(number1=0,number2=0):
    sum1 = int(number1)+int(number2)
    return  render_template("calc.html", title="Addition", foo=number1, foos=number2, operator="Addition", answer=sum1)

@app.route("/subtract/<number1>/<number2>/")
def subtract(number1=0,number2=0):
    result1 = int(number1)-int(number2)
    return  render_template("calc.html", title="Subtraction", foo=number1, foos=number2, operator="Subtraction", answer=result1)

@app.route("/multiply/<number1>/<number2>/")
def multiply(number1=0,number2=0):
    quotient1 = int(number1)*int(number2)
    return  render_template("calc.html", title="Multiplication", foo=number1, foos=number2, operator="Multiplication", answer=quotient1)

@app.route("/divide/<number1>/<number2>/")
def divide(number1=0,number2=0):
    division_sum1 = int(number1)/int(number2)
    return  render_template("calc.html", title="Division", foo=number1, foos=number2, operator="Division", answer=division_sum1)


if  __name__ == "__main__":
    app.run()
