from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db

from models import CategoryModel
from schemas import PlainCategorySchema

blp = Blueprint("Categories", "categories", description="Operation on categories")



@blp.route("/category/<int:category_id>")
class Category(MethodView):
    @blp.response(200, PlainCategorySchema)
    def get(self, category_id):
        category = CategoryModel.query.get_or_404(category_id)
        return category
    
    def delete(self, category_id):
        category = CategoryModel.query.get_or_404(category_id)

        db.session.delete(category)
        db.session.commit()

        return {"message": "Category deleted "}


@blp.route("/category")
class CategoriesList(MethodView):
    @blp.response(200, PlainCategorySchema(many=True))
    def get(self):
        category = CategoryModel.query.all()
        if len(category) == 0:
            abort(404, message="There are not categories yet available")
        else:
            return category

    @blp.arguments(PlainCategorySchema)
    @blp.response(201, PlainCategorySchema)
    def post(self, category_data):
        category = CategoryModel(**category_data)
        try:
            db.session.add(category)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the item")

        return category