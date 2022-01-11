from db import db
import datetime
from sqlalchemy.sql import func


class Name(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=func.now())
