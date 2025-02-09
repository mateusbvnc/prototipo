from app import db
from flask_login import UserMixin

class usuario(db.Model, UserMixin):

    __tablename__ = "Usuarios"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nome = db.Column(db.String(150), nullable = False)
    email = db.Column(db.String(150), nullable = False)
    senha = db.Column(db.String(20), nullable = False)

    def __init__(self, **atributos):

        self.nome = atributos["nome"]
        self.email = atributos["email"]
        self.senha = atributos["senha"]