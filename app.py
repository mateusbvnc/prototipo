from flask import Flask, request, render_template, redirect,url_for
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
'''****************************************************************************************************'''
app = Flask(__name__)

from .app_config import * # carrega todas as confiracoes de app
'''****************************************************************************************************'''
db = SQLAlchemy(app)

from .models import * # carrega todos os modelos

with app.app_context():
    db.create_all() # cria o banco de dados se não existir  
'''****************************************************************************************************'''
login_manager = LoginManager(app) # gerenciador de usuário


@login_manager.user_loader
def load_user(id):
    return usuario.query.get(id)

'''****************************************************************************************************'''
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method == "POST":    
        email = request.form["email"]
        senha = request.form["senha"]
        user = usuario.query.filter(usuario.email == email, usuario.senha == senha).first()
        if(user):
            login_user(user)
            return redirect(url_for("tabelas"))
        else:
            return render_template("login.html",erro="Email ou Senha inválido")

    return render_template("login.html",erro="")


@app.route("/rastreamento")
def rastreamento():
    return render_template("rastreamento.html")

@app.route("/tabelas", methods=['GET'])
@login_required
def tabelas():
    lista = contratacao.query.all()
    return  render_template("tables.html",lista=lista)


@app.route("/tabelas/<id>", methods = ["GET", "POST"])
@login_required
def Contratacao(id):
    if request.method == "POST":
        status = request.form.get("opcao")
        contract = contratacao.query.get(id)
        contract.status = status
        db.session.commit()
        return redirect(url_for("tabelas"))
    contract = contratacao.query.get(id)
    return render_template("contratacao.html", contratacao = contract)

@app.route("/tabelas/novacontratacao",methods = ["GET","POST"])
@login_required
def novaLinha():
    if request.method == "POST":
        titular = request.form.get("titular")
        entrada = datetime.strptime(request.form.get("entrada"), '%Y-%m-%d').date()
        processo = request.form.get("processo")
        status = "Em análise"
        c = contratacao(titular = titular, entrada = entrada, processo = processo, status = status)
        db.session.add(c)
        db.session.commit()
        return redirect(url_for("tabelas"))
    return render_template("nova.html")

