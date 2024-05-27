from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

db_config={
    'host': 'bd',
    'user': 'edu',
    'password': '1234',
}

conn = mysql.connector.connect(**db_config)

@app.route('/')
def index():
    cursor = conn.cursor()
    cursor.execute("USE Desafio4")
    cursor.execute("SELECT * FROM usuario")
    desafio4 = cursor.fetchall()
    cursor.close()
    return render_template('index.html', desafio4=desafio4)

@app.route('/Contatos')
def Contatos():
    return render_template('Contatos.html')

@app.route('/Procurados')
def Procurados():
    return render_template('Procurados.html')

@app.route('/add', methods=['POST'])
def add_infor():
    if request.method == 'POST':
        user_nome = request.form['user_nome']
        user_email = request.form['user_email']
        user_tell = request.form['user_tell']
        cursor = conn.cursor()
        cursor.execute("USE Desafio4")
        cursor.execute("INSERT INTO usuario (user_nome, user_email, user_tell) VALUES (%s, %s ,%s )", (user_nome, user_email, user_tell))
        conn.commit()
        cursor.close()
        return redirect(url_for('exibir_dados'))

@app.route('/dados')
def exibir_dados():
    cursor = conn.cursor()
    cursor.execute("USE Desafio4")
    cursor.execute("SELECT * FROM usuario")
    dado = cursor.fetchall()
    print (type(dado))
    print (dado)
    cursor.close()
    return render_template('dados.html', dado=dado)
    
    
if __name__ == '__main__':
    app.run(debug=True)