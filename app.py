from datetime import datetime
from random import randint
from urllib import request

from flask import Flask, render_template, request

app = Flask(__name__)

'https://ww.google.com/search?q='


@app.route('/')
def hello_world():
    return "<p>Hello, World! Yolo</p>"


@app.route('/hello/<username>')
def name(username):
    return username


@app.route('/time')
def timemachine():
    return str(datetime.time(datetime.now()))


@app.route('/data')
def datamachine():
    return str(datetime.date(datetime.now()))


@app.route('/licz/<int:liczba1>/<int:liczba2>')
def dodawanie(liczba1, liczba2):
    return str(liczba1 + liczba2)


@app.route('/losuj')
def random_3():
    digits = []

    for d in range(3):
        digits.append(str(randint(0, 9)))

    return ''.join(digits)

@app.route('/lotek')
def random_6():
    digits2 = []

    while len(digits2) <= 6:
        digit = str(randint(1, 49))
        if digit not in digits2:
            digits2.append(digit)

    return ' - '.join(digits2)

## return shuffle(list(range(1, 50))[:6]   losuje liczbe z przedialu


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        first_name = request.form.get("firstName")
        return render_template("confirmation.html", first_name=first_name)
    return render_template("form.html")


operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a + b,
    "*": lambda a, b: a + b,
    "/": lambda a, b: a + b,
}

@app.route("/calc", methods=["GET", "POST"])
def calculate():
    result = ''

    if request.method == "POST":
        try:
            digit1 = request.form.get("digit1")
            digit2 = request.form.get("digit2")
            operation = request.form.get("operation")
        except ValueError:
            return render_template("kalku.html", message="Podaj pop liczby!")

        result = operations.get(operation)(digit1, digit2)

    return render_template("kalku.html", result=result)



@app.route("/meth", methods=["GET", "POST"])
def meth():
    if request.method == "POST":
        return "Wyslales POST"
    return "wyslales GET"











