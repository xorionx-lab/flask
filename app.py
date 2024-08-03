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


@app.route('/deletar_contato', methods=['POST'])
def deletar_contato():
    email = request.form['email']
    contato = session.query(Contato).filter_by(email=email).first()
    if contato:
        session.delete(contato)
        session.commit()
    return redirect('/')


@app.route('/editar_contato', methods=['POST'])
def editar_contato():
    contato_id = request.form['id']
    contato = session.query(Contato).get(contato_id)
    if contato:
        contato.nome = request.form['nome']
        contato.email = request.form['email']
        contato.celular = request.form['celular']
        contato.celular_alt = request.form.get('celular_alt', '')
        contato.tags = request.form['tags']
        session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)