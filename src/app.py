from flask import Flask, render_template
from src.common.database import Database
from src.views.alerts import alert_blueprint
from src.views.stores import store_blueprint
from src.views.users import user_blueprint

__author__ = 'bpt'


app = Flask(__name__)
app.config.from_object('src.config')
app.secret_key = '123'


@app.before_first_request
def init_db():
    Database.initialize()


@app.route('/')
def home():
    return render_template('home.html')


app.register_blueprint(alert_blueprint, url_prefix='/alerts')
app.register_blueprint(store_blueprint, url_prefix='/stores')
app.register_blueprint(user_blueprint, url_prefix='/users')

if __name__ == '__main__':
    app.run(debug=True)

