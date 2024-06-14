from models import db, Incident
from db import db

def create_incident(description, severity):
    incident = Incident(description=description, severity=severity)
    db.session.add(incident)
    db.session.commit()
    return incident
