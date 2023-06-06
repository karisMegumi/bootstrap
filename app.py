import mysql.connector
from flask import Flask, render_template, request, url_for, flash, redirect, session
from forms import formLogin, formNovoUsuario 
from hashlib import sha256

app = Flask(__name__)

app.config['SECRET_KEY'] = '7272a66ced14923d1b441924bef72d1f'

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'P@$$w0rd',
    database = 'ead_senac',
)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/contato')
def contato():
    return render_template("contato.html")

@app.route('/cursos')
def cursos():
    return render_template("cursos.html")

@app.route('/login', methods=['get','post'])
def login():
    titulo = 'Login de acesso'
    descricao = 'Formulario de login'

    form_login = formLogin()
    form_novo_usuario = formNovoUsuario()

    if form_login.validate_on_submit() and 'submitLogin' in request.form:
        flash(f'Login realizado com sucesso: {form_login.email.data}', 'alert-success')
        return redirect(url_for('index'))
    
    if form_novo_usuario.validate_on_submit() and 'submit' in request.form:
        cursor = mysql.cursor()

        nome = form_novo_usuario.nome.data
        telefone = form_novo_usuario.celular.data
        Email = form_novo_usuario.Email.data
        cpf = form_novo_usuario.cpf.data
        Senha = form_novo_usuario.Senha.data
        hashSenha = sha256(Senha.encode())

        query = f'INSERT INTO alunos (nome, email, celular, documento, senha) VALUES ("{nome}", "{Email}", "{telefone}", "{cpf}", "{hashSenha.hexdigest()}")'
        cursor.execute(query)
        mydb.commit()

        flash(f'CADASTRO REALIZADO COM SUCESSO: {form_novo_usuario.nome.data}', 'alert success')
        return redirect(url_for('index'))

    return render_template("login.html", descricao = descricao, form_login = form_login, form_novo_usuario = form_novo_usuario)

@app.route('/ead')
def ead():
    return render_template("ead.html")

if __name__ == '__main__':
    app.run(debug=True)