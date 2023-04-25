from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db

from models import PostModel, UserModel
from schemas import PostSchema

blp = Blueprint("Posts","posts", description="Operation on posts")

@blp.route("/post/<int:post_id>")
class Post(MethodView):
    @blp.response(200, PostSchema)
    def get(self,post_id):
        post = PostModel.query.get(post_id)
        if post is None:
            abort(404, message="Post not found")
        else:
            return post
    
    def delete(self,post_id):
        post = PostModel.query.get(post_id)
        
        db.session.delete(post)
        db.session.commit()
        return {"message": "Post deleted successfully"}
    
@blp.route("/post")
class PostList(MethodView):
    @blp.response(200, PostSchema(many=True))
    def get(self):
        post = PostModel.query.all()
        if len(post) == 0:
            abort(404, message="There are not posts yet available")
        else:
            return post
    
    @blp.arguments(PostSchema)
    @blp.response(201, PostSchema)
    def post(self,post_data):
        post = PostModel(**post_data)
        try:
            db.session.add(post)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting post")

        return post
    
@blp.route("/postbycat/<int:category_id>")
class PostByCategory(MethodView):
    @blp.response(200, PostSchema(many=True))
    def get(self, category_id):
        post = PostModel.query.filter_by(category_id=category_id).all()
        if len(post) == 0:
            abort(404, message="There are not posts yet available")
        else:
            return post


@blp.route("/post/<int:post_id>/user/<int:user_id>")
class LinkPostToUser(MethodView):
    @blp.response(201, PostSchema)
    def post(self, post_id, user_id):
        post = PostModel.query.get_or_404(post_id)
        user = UserModel.query.get_or_404(user_id)

        post.users.append(user)

        try:
            db.session.add(post)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the user.")

        return user