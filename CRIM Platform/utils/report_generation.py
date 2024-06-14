from flask import Flask, jsonify
from models import Incident
import pandas as pd

def generate_report():
    incidents = Incident.query.all()
    report = []
    for incident in incidents:
        report.append({
            'id': incident.id,
            'description': incident.description,
            'severity': incident.severity,
            'status': incident.status,
            'assigned_to': incident.assigned_to,
            'created_at': incident.created_at,
            'updated_at': incident.updated_at
        })
    return report
