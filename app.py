from flask import Flask, render_template, request, redirect, session as flask_session
from database import User, Contato, session
from werkzeug.security import generate_password_hash, check_password_hash
import os


app = Flask(__name__)
app.secret_key = os.urandom(24)



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        new_user = User(username=username, password=hashed_password)
        session.add(new_user)
        session.commit()
        return redirect('/login')

    return render_template('register.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


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