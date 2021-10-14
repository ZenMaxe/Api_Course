from flask_sqlalchemy import SQLAlchemy

from app import app

db = SQLAlchemy(app)


class Members:
    
    members_id = db.Column(db.Integer(), unique=True, nullable=False)
    members_username = db.Column(db.String(32), primary_key=True)
