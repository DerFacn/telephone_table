import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ChangeThisLater'
    BASIC_AUTH_USERNAME = os.environ.get('BASIC_AUTH_USERNAME') or 'nikita'
    BASIC_AUTH_PASSWORD = os.environ.get('BASIC_AUTH_PASSWORD') or 'nikita'
    ALCHEMICAL_DATABASE_URL = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    CITIES = os.environ.get('CITIES') or ['Meldorf', 'Heide']
