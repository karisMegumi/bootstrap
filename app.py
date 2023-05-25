from flask import Flask, render_template, request
from forms import formLogin, formNovoUsuario 

app = Flask(__name__)

app.config['SECRET_KEY'] = '7272a66ced14923d1b441924bef72d1f'


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

    return render_template("login.html", descricao = descricao, form_login = form_login, form_novo_usuario = form_novo_usuario)

@app.route('/ead')
def ead():
    return render_template("ead.html")

if __name__ == '__main__':
    app.run(debug=True)