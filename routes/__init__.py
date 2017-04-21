
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from answers import crit_api
from criteria import criteria_api
from artifacts import artifact_api
from tasks import task_api
from evalmodes import eval_mode_api

app = Flask(__name__, template_folder='../templates')
app.register_blueprint(crit_api)
app.register_blueprint(criteria_api)
app.register_blueprint(artifact_api)
app.register_blueprint(task_api)
app.register_blueprint(eval_mode_api)


#Include config from config.py
app.config.from_object('config')

#Create an instance of SQLAclhemy
db = SQLAlchemy(app)



@app.route('/', methods=['GET'])
def help():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3006, threaded=True)




