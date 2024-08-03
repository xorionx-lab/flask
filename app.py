from flask import Flask, rende_template, request, redirect
from database import Contato, session


app = Flask(__name__)


@app.route('/')
def index():
    contatos = session.query(Contato).all()
    return rende_template('index.html', contatos=contatos)