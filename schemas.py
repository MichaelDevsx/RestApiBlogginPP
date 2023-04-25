from marshmallow import Schema, fields

class PlainUserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    email = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    date_reg = fields.Date()
    
class PlainPostSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    content = fields.Str()
    date_post = fields.Date()

class PlainCommentSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    email = fields.Str(required=True)
    comment = fields.Str()

class PlainCategorySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    description = fields.Str()


class UserSchema(PlainUserSchema):
    posts = fields.List(fields.Nested(PlainPostSchema()),dump_only=True)

class PostSchema(PlainPostSchema):
    users = fields.List(fields.Nested(PlainUserSchema()),dump_only=True)
    category_id = fields.Int(load_only=True)

class CommentSchema(PlainCommentSchema):
    post_id = fields.Int(load_only=True)

class UserPostSchema(Schema):
    message = fields.Str()
    user = fields.Nested(UserSchema)
    tag = fields.Nested(PostSchema)