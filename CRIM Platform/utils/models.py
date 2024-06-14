from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from db import db


class Incident(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200))
    severity = db.Column(db.String(50))
    status = db.Column(db.String(50), default='Open')
    assigned_to = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
