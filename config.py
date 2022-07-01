import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    """
    Set Config variables for the flask app.
    Using Environment variables where available otherwise
    create the config variable if not done already.
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Random string'
