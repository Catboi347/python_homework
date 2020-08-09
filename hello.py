import random
from flask import Flask
app = Flask(__name__)

@app.route("/")
def beginning():
   return "<H1>Select a number between 1 to 4 including 1 and 4.</H1>"

@app.route("/<int:number>")
def numberchoice(number):
   if number == 1:
      return "<H1>You will be served Breakfast</H1>"
   if number == 2:
      return "<H1>You will be served Lunch</H1>"
   if number == 3:
      return "<H1>You will be sereved dinner</H1>"
   if number == 4:
      return "<H1>You will be served dessert</H1>"
   return ("<H1>You chose number%d</H1>") %number 

@app.route("/cats")
def cats():
   return "<H1>cats are cool!</H1>"

@app.route("/number<int:integer")
def number1(integer):
   print ("<H1>choose an integer</H1>")
   return "<H1>You chose the integer%d</H1>" %integer

@app.route("/play")
def play():
   return "<H1>I am playing!</H1>"

@app.route("/sleep")
def sleep():
   return "<H1>The cat and I are sleeping</H1>"

@app.route("/eat")
def eat():
   return "<H1>cereal is great to eat</H1>"

@app.route("/talk/<int:duration>")
def talk(duration):
   interval = "minutes" 
   return "<H1>talk duration:%d %s</H1>" %(duration, interval)

@app.route("/fun")
def fun():
   return "<H1>I am having fun</H1>"

@app.route("/happy/dog/<name>")
def happy(name):
   return "<H1>This is a dog:" + name + "</H1>"

if __name__ == '__main__':
   app.run()






#ask for a number 
#print the number they picked and tell them you got this number
#
