from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome')
def return_welcome():
    return "Welcome"

@app.route('/welcome/home')
def return_welcome_home():
    return "Welcome home"

@app.route('/welcome/back')
def return_welcome_back():
    return "Welcome back"