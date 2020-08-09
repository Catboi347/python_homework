from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)
@app.route("/")
def main():
    return "Hello world"

@app.route("/hello")
def hello():
    return "hello"

@app.route("/members/<string:name>/")
def members(name):
    return  render_template('som.html',name=name)

if  __name__ == "__main__":
    app.run()