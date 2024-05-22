import  os
from flask import Flask, redirect, render_template, request, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "@D5d52811"
app.config['MYSQL_DB'] = "Desafio4"

mysql = MySQL(app)


@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuario")
    desafio4 = cur.fetchall()
    cur.close()
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
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO usuario (user_nome, user_email, user_tell) VALUES (%s, %s ,%s )", (user_nome, user_email, user_tell))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('exibir_dados'))

@app.route('/dados')
def exibir_dados():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuario")
    dado = cur.fetchall()
    print (type(dado))
    print (dado)
    cur.close()
    return render_template('dados.html', dado=dado)
    
    
if __name__ == '__main__':
    app.run(debug=True)