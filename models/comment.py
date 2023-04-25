from db import db

class CommentModel(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    comment = db.Column(db.String(255), nullable=False)

    post_id = db.Column(db.Integer(), db.ForeignKey("posts.id"), nullable=False)