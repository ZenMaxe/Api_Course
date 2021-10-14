from app import db


class Posts(db.Model):
    from_user = db.Column(db.Integer(), nullable=False)
    post_id = db.Column(db.Integer(), primary_key=True)
    likes = db.Column(db.Integer(), nullable=True)
    comments = db.Column(db.Integer(), nullable=True)
    caption = db.Column(db.String(), nullable=False)
    followers = db.Column(db.Integer(), nullable=True)
    name = db.Column(db.String(), nullable=False)
    like_from = db.Column(db.Integer(), nullable=False)
