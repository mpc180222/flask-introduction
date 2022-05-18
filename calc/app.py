from operations import add, sub, mult, div
from flask import Flask, request

app = Flask(__name__) 

@app.route('/add')
def return_add():
    a = request.args.get('a',type=int)
    b = request.args.get('b',type=int)
    return str(add(a,b))


@app.route('/sub')
def return_sub():
    a = request.args.get('a',type=int)
    b = request.args.get('b',type=int)
    return str(sub(a,b))

@app.route('/mult')
def return_mult():
    a = request.args.get('a',type=int)
    b = request.args.get('b',type=int)
    return str(mult(a,b))

@app.route('/div')
def return_div():
    a = request.args.get('a',type=int)
    b = request.args.get('b',type=int)
    return str(div(a,b))

@app.route('/math/add')
def return_add2():
    a = request.args.get('a',type=int)
    b = request.args.get('b',type=int)
    return str(add(a,b))


@app.route('/math/sub')
def return_sub2():
    a = request.args.get('a',type=int)
    b = request.args.get('b',type=int)
    return str(sub(a,b))

@app.route('/math/mult')
def return_mult2():
    a = request.args.get('a',type=int)
    b = request.args.get('b',type=int)
    return str(mult(a,b))

@app.route('/math/div')
def return_div2():
    a = request.args.get('a',type=int)
    b = request.args.get('b',type=int)
    return str(div(a,b))