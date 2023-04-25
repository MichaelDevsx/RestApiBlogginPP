from db import db
from sqlalchemy import DateTime, func

class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True ,nullable=False)
    password = db.Column(db.String(), nullable=False)
    date_reg = db.Column(DateTime(timezone=True), server_default=func.now())

    posts = db.relationship("PostModel", back_populates="users", secondary="users_posts", lazy="dynamic", cascade="all, delete")

