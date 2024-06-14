from flask import Flask, request, jsonify  # Add jsonify to the import statement
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import Incident
from monitoring_tools import fetch_data_from_tool
from anomaly_detection import train_anomaly_detector, detect_anomalies
from incident_manager import create_incident
from ticket_assignment import train_ticket_assignment_model, predict_officer
from resolution_tracking import update_ticket_status
from notifier import send_email, send_sms
from db import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

def load_or_train_models():
    try:
        training_data = fetch_data_from_tool('https://api.yourdatasource.com/training_data', 'your_api_key')
        labels = training_data['labels']  # Ensure that your training data includes 'labels'
        anomaly_model = train_anomaly_detector(training_data)
        ticket_assignment_model = train_ticket_assignment_model(training_data, labels)
    except Exception as e:
        print(f"Error fetching training data: {e}")
        anomaly_model = None  # Default or previously trained model
        ticket_assignment_model = None  # Default or previously trained model
    return anomaly_model, ticket_assignment_model

anomaly_model, ticket_assignment_model = load_or_train_models()

@app.route('/monitor', methods=['GET'])
def monitor():
    data = fetch_data_from_tool('https://api.monitoringtool.com/data', 'your_api_key')
    anomalies = detect_anomalies(anomaly_model, data)
    for anomaly in anomalies:
        incident = create_incident('Anomaly detected', 'High')
        officer = predict_officer(ticket_assignment_model, anomaly)
        update_ticket_status(incident.id, 'Assigned', officer)
        send_email('officer@example.com', 'New Incident', f'Incident {incident.id} assigned to you')
        send_sms('+1234567890', f'Incident {incident.id} assigned to you')
    return jsonify({'message': 'Monitoring complete'})

@app.route('/assign/<int:incident_id>', methods=['POST'])
def assign(incident_id):
    officer = request.json.get('officer')
    incident = update_ticket_status(incident_id, 'Assigned', officer)
    if incident:
        return jsonify({'message': 'Ticket assigned', 'incident': incident.id})
    return jsonify({'message': 'Incident not found'}), 404

@app.route('/status/<int:incident_id>', methods=['GET'])
def status(incident_id):
    incident = Incident.query.get(incident_id)
    if incident:
        return jsonify({'id': incident.id, 'status': incident.status, 'assigned_to': incident.assigned_to})
    return jsonify({'message': 'Incident not found'}), 404

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

@app.route('/report', methods=['GET'])
def report():
    report_data = generate_report()
    return jsonify(report_data)

if __name__ == '__main__':
    app.run(debug=True)
