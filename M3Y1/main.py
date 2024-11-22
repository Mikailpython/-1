import random
from flask import Flask

app = Flask(__name__)

facts_list = ["""Орел""", """Решка"""]

@app.route("/")
def hello_world():
    return f'<h1>Привет! здесь ты можеш поиграть монетку.</h1><a href="/random_fact">Играть!</a>'
 

@app.route("/random_fact")
def bye_world():
    return f'<p>{random.choice(facts_list)}</p>'

app.run(debug=True)


