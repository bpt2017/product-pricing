from src.app import app

__author__ = 'bpt'

app.run(debug=app.config['DEBUG'], port=4990)