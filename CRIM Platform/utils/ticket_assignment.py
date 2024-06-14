from sklearn.ensemble import RandomForestClassifier
import pandas as pd

def train_ticket_assignment_model(training_data, labels):
    model = RandomForestClassifier()
    model.fit(training_data, labels)
    return model

def predict_officer(model, incident_features):
    officer = model.predict([incident_features])
    return officer[0]
