from flask import Flask, render_template, redirect, request, flash
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

load_dotenv() 
app = Flask(__name__)
app.secret_key = 'magapp'

mail= Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] =os.getenv("email")
app.config['MAIL_PASSWORD'] =os.getenv("senha")
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


class Contato:
    def __init__(self, nome, email, mensagem):
        self.nome = nome
        self.email = email
        self.mensagem = mensagem

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        formContato = Contato(
            request.form["nome"],
            request.form["email"],
            request.form["mensagem"]
        )

        msg = Message('Hello', sender = 'magu1908.contato.teste@gmail.com', recipients = ['magu1908.contato.teste@gmail.com'])
        msg.body = "Hello Flask message sent from Flask-Mail"

        mail.send(msg)
        flash('Mensagem enviada com sucesso!')
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

