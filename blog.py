from flask import Flask, flash, redirect, render_template, request, session, abort
from app import app

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    bar = {'username': 'Miguel','age': 23}
    return render_template('blog_index.html', title='Home', foo=bar)

@app.route("/members/<string:name>/")
def members(name):
    return  render_template('member.html',member=name)

if  __name__ == "__main__":
    app.run()