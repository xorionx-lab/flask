from flask import Flask, render_template, request, redirect
from database import Contato, session


app = Flask(__name__)


@app.route('/')
def index():
    contatos = session.query(Contato).all()
    return render_template('index.html', contatos=contatos)

@app.route('/salvar_contato', methods=['POST'])
def salvar_contato():
    novo_contato = Contato(
        nome = request.form['nome'],
        email = request.form['email'],
        celular = request.form['celular'],
        celular_alt = request.form.get('celular_alt', ''),
        tags = request.form['tags'],
    )
    session.add(novo_contato)
    session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)