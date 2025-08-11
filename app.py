from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
load_dotenv('development.env')
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("pages/index.html")

@app.route('/login' , methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("pages/login.html")
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()