from flask import render_template, request, redirect, url_for, flash, Blueprint
from Create_Map import app
from Create_Map import db
from .models import Account_user
from flask_login import login_user
from .forms import RegisterForm, LoginForm




@app.route('/')
def temp():
    return render_template("public/temp.html")


@app.route('/create_account', methods = ["POST","GET"])
def create_account():
    form = RegisterForm()
    
    if form.validate_on_submit():
        user = Account_user(name = form.name.data, surname = form.surname.data, password = form.password.data, confirm_pass = form.confirm_password.data, email = form.email.data, phone = form.phone.data )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('public/login'))

    
    return render_template('public/create_account.html', form = form)

@app.route('/login', methods = ['POST','GET'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = Account_user.query.filter_by(email = form.email.data).first()

        if user and user.password == form.password.data:
            login_user(user)
            return render_template("public/temp.html")

        else:
            flash(f'Login unsuccesful','danger')

    return render_template('public/login.html')