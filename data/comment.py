from app import db


class Comments(db.Model):
    comment = db.Column(db.String(), nullable=False)
    comment_for_post = db.Column(db.Integer(), nullable=False)
    comment_from_user = db.Column(db.Integer(), nullable=False)
    comment_id = db.Column(db.Integer(), nullable=False, primary_key=True)
