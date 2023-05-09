from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/contato')
def contato():
    return render_template("contato.html")

@app.route('/cursos')
def cursos():
    return render_template("cursos.html")

@app.route('/base')
def base():
    return render_template("base.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/sobreEAD')
def sobreEAD():
    return render_template("sobreEAD.html")



if __name__ == '__main__':
    app.run(debug=True)