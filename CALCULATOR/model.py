from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Materials_sql(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(120), unique=True)
    material = db.Column(db.String(120), unique=True)