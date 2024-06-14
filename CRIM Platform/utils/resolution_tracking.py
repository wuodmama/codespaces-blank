from models import Incident
from db import db

def update_ticket_status(incident_id, status, assigned_to=None):
    incident = Incident.query.get(incident_id)
    if incident:
        incident.status = status
        if assigned_to:
            incident.assigned_to = assigned_to
        db.session.commit()
        return incident
    return None
