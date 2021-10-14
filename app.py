from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///api_course.sqlite'
db = SQLAlchemy(app)

from Url.User import *

if __name__ == '__main__':
    app.run()
