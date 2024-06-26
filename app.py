from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

import os

app = Flask(__name__)
app.config.from_pyfile("config.py")
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)



from routes import *

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)