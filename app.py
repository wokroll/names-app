from flask import Flask, render_template, request
from models import Name
from db import db

import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template("index.jinja")


@app.route('/', methods=["POST"])
def enter_name():
    form_name = str(request.form['name'])
    name_in_db = Name.query.filter_by(name=form_name).first()

    if name_in_db:
        result = "Already seen you " + form_name
    else:
        new_name = Name(name=form_name)
        db.session.add(new_name)
        db.session.commit()
        result = "Hello, " + form_name

    return render_template("checked_name.jinja", result=result)


@app.route('/names')
def all_names():
    names = db.session.query(Name).all()
    return render_template("all_names.jinja", names=names)


if __name__ == '__main__':
    #app.run(host='0.0.0.0')
    app.run( host='0.0.0.0', port=5000)
