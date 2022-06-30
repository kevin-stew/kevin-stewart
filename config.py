import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    """
    Set Config variables for the flask app.
    Using Environment variables where available otherwise
    create the config variable if not done already.
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')

    #mail credentials
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT'))
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL') 
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') 
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_SENDTO = os.environ.get('MAIL_SENDTO')
    # administrator list
    ADMINS = ['kstewar2@gmail.com']
        
        

