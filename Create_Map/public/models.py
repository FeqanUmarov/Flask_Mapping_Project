from Create_Map import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Account_user.query.get(user_id)

class Account_user(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(40))
    surname = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    confirm_pass = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

    def __init__(self, _name, _surname, _password, _confirm_pass, _email, _phone):
        self.name = _name
        self.surname = _surname
        self.password = _password
        self.confirm_pass = _confirm_pass
        self.email = _email
        self.phone = _phone

