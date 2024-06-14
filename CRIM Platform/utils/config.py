import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'supersecretkey'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///platform.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
    EMAIL_SENDER = os.environ.get('EMAIL_SENDER')
    EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
    SMTP_SERVER = os.environ.get('SMTP_SERVER', 'smtp.example.com')
    SMTP_PORT = int(os.environ.get('SMTP_PORT', 587))

