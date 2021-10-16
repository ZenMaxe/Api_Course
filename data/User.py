from app import app, db


class Users(db.Model):
    email = db.Column(db.String(110), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False, unique=True)
    name = db.Column(db.String(80), nullable=False)
    id = db.Column(db.Integer(), primary_key=True)
    comments = db.Column(db.Integer(), nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username
