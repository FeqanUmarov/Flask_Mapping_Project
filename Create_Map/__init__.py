from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager


app = Flask(__name__)
app.secret_key = "Secret_Key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db" 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager(app)




from Create_Map.admin import routes

from Create_Map.public import routes


