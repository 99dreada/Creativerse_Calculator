from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Process_sql(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)

class Materials_sql(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(120), nullable=False)
    material = db.Column(db.String(120), nullable=False)
    colour = db.Column(db.String(120), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    units = db.Column(db.Integer, nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    process_id =  db.Column(db.Integer, db.ForeignKey(Process_sql.id), nullable=False)

class Machines_sql(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    size = db.Column(db.String(120), nullable=False)
    watt_hours = db.Column(db.Integer, nullable=False)
    machine_cost = db.Column(db.Integer, nullable=False)

class Other_sql(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    value = db.Column(db.Integer, nullable=False)

class Products_sql(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(120),unique=True, nullable=False)

"""
INIT DATABASE
"""

INIT_TABLES = [
    Process_sql
]
INIT_DIRECTORY_NAME = "CALCULATOR/db/initial"
TABLES_TO_SAVE = [
    Materials_sql,
    Machines_sql,
    Other_sql,
    Products_sql
]

def create_db():
    try: db.drop_all()
    except: pass
    db.create_all()
    import csv
    import os
    for table in INIT_TABLES:
        filename = table.__name__ + '.csv'
        filename = os.path.join(INIT_DIRECTORY_NAME, filename)
        with open(filename, newline='') as file:
            for row in csv.DictReader(file):
                db.session.add(table(**row))
    db.session.commit()