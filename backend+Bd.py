from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def criar_bd():
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT,
            senha TEXT,
            nascimento TEXT,
            telefone TEXT,
            endereco TEXT,
            sexo TEXT,
            cpf TEXT,
            cidade TEXT,
            estado TEXT\
        )
    ''')
    conn.commit()
    conn.close()

criar_bd()

@app.route('/')
def index():
    return render_template('cadastro.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    dados = (
        request.form['nome'],
        request.form['email'],
        request.form['senha'],
        request.form['nascimento'],
        request.form['telefone'],
        request.form['endereco'],
        request.form['sexo'],
        request.form['cpf'],
        request.form['cidade'],
        request.form['estado']
    )

    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute('INSERT INTO usuarios (nome, email, senha, nascimento, telefone, endereco, sexo, cpf, cidade, estado) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', dados)
    conn.commit()
    conn.close()

    return "✅ Cadastro realizado com sucesso!"

if __name__ == '__main__':
    app.run(debug=True)
