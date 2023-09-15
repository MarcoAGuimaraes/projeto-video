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
        
        msg = Message(subject = f'{formContato.nome} te enviou uma mensagem no portfólio', sender = app.config.get("MAIL_USERNAME"), recipients= ['magu1908@gmail.com', app.config.get("MAIL_USERNAME")],body = f'''
        {formContato.nome} com o e-mail {formContato.email}, te enviou a seguinte mensagem:

        {formContato.mensagem}

        '''
        )
		
		
        mail.send(msg)
        flash('Mensagem enviada com sucesso!')
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

