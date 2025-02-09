from ..app import db

class contratacao(db.Model):

    __tablename__ = "Contratacoes"

    id = db.Column(db.Integer,primary_key = True, autoincrement = True)
    entrada = db.Column(db.Date)
    titular = db.Column(db.String(150),nullable = False)
    auxiliar = db.Column(db.String(150))
    processo = db.Column(db.String(50),unique = True)
    status = db.Column(db.String(200), nullable = False)

    def __init__(self, **atributos):
        self.entrada = atributos.get("entrada")
        self.titular = atributos.get("titular")
        self.auxiliar = atributos.get("auxiliar")
        self.processo = atributos.get("processo")
        self.status = atributos.get("status")