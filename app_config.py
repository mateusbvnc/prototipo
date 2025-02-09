from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///fiocruz.db"
app.config["SECRET_KEY"] = "prototipo"