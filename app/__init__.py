from flask import Flask, Blueprint

from config import Config
from .site.routes import site
from .project.routes import project

app = Flask(__name__)

app.register_blueprint(site)
app.register_blueprint(project)

app.config.from_object(Config)