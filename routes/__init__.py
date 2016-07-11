
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from model import *
from critiques import crit_api
from criteria import criteria_api
from artifacts import artifact_api

app = Flask(__name__)
app.register_blueprint(crit_api)
app.register_blueprint(criteria_api)
app.register_blueprint(artifact_api)

#Include config from config.py
app.config.from_object('config')

#Create an instance of SQLAclhemy
db = SQLAlchemy(app)


if __name__ == '__main__':
    app.run()




