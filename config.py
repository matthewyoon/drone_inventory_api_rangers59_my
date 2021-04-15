import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Giving access to the project in ANY OS we find ourselves in
# Allow outside files and folders to have the ablity to add to the project from
# The base directory

class Config():
    """
    We will set Config variables for the Flask App here.
    Using Environment variables where available, otherwise
    we will create the config variable(s) if not already done.
    """

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'You will never guess...'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Turn off update messages from the database