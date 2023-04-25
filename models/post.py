from db import db
from sqlalchemy import DateTime, func

class PostModel(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    date_post = db.Column(DateTime(timezone=True), server_default=func.now())
    category_id = db.Column(db.Integer(), db.ForeignKey("categories.id"), nullable=False)
    
    users = db.relationship("UserModel", back_populates="posts", secondary="users_posts", lazy = "dynamic")
