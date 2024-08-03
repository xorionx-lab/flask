from flask import Flask, render_template, request, redirect
from database import Contato, session


app = Flask(__name__)


@app.route('/')
def index():
    contatos = session.query(Contato).all()
    return render_template('index.html', contatos=contatos)

if __name__ == '__main__':
    app.run(debug=True)