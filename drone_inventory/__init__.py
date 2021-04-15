from flask import Flask
from config import Config

from .site.routes import site
from .authentication.routes import auth
from .api.routes import api

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .models import db as root_db, login_manager, ma

# Import for Flask-Marshmallow
from flask_marshmallow import Marshmallow

from flask_cors import CORS #Cross Origin Resource Sharing - so that we don't have malicious people sending stuff
#Origin stands for domain - we're now allowing browsers to share resources between various domains. If we did opens ourselves up to malware
from .helpers import JSONEncoder

app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api)

root_db.init_app(app)
migrate = Migrate(app, root_db)

login_manager.init_app(app) # Attaches the login_manager to our app
login_manager.login_view = 'auth.signin' # Specifies what page to load for NON-authed users - redirects to signin

ma.init_app(app)

CORS(app)

app.json_encoder = JSONEncoder

from drone_inventory import models