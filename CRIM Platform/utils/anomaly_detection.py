import numpy as np
from sklearn.ensemble import IsolationForest
import pandas as pd

def train_anomaly_detector(data):
    model = IsolationForest(contamination=0.01)
    model.fit(data)
    return model

def detect_anomalies(model, data):
    predictions = model.predict(data)
    anomalies = np.where(predictions == -1)
    return anomalies
