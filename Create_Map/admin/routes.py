from flask import render_template,  request, redirect, url_for, flash, Blueprint
from Create_Map import app


@app.route('/index')
def index():
    return render_template("admin/index.html")

