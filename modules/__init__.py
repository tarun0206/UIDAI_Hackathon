from flask import Flask, app

app = Flask(__name__)
from modules.uidai.routes import uidai_module
app.register_blueprint(uidai.routes.uidai_module, url_prefix = '/')