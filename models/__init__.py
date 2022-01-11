from db import db
import datetime


class Name(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())
