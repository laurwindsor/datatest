from flask import request
from flask_restplus import Resource, fields
from doh import expand

from {{cookiecutter.app_name}}.storage.tags import get_tag, put_tag


def get_tag_fields():
    return {
        'name': fields.String(
            required=True,
            max_length=256,
            description='The name of the tag'),
        'description': fields.String(
            required=False,
            max_length=512,
            description='A description of the tag'),
        'client_data': fields.String(
            required=False,
            max_length=64,
            description='A slot for the creator to store a token, or rubric'),
        'expiry_seconds': fields.Integer(
            required=True,
            description='How long are values in this tag valid?'),
        'public': fields.Boolean(
            required=True,
            default=False,
            description='Is this visible beyond its creator? See `created_by`'),
    }


def init_app(app, api):
    tag_model = api.model('WriteTag', get_tag_fields())

    @api.route('/tag')
    class TagCreate(Resource):
        @api.expect(tag_model, validate=True)
        def post(self):
            tag = request.get_json()
            return expand(put_tag(tag)), 201

    @api.route('/tag/<uuid:tag_id>')
    class TagRead(Resource):
        def get(self, tag_id):
            from {{cookiecutter.app_name}}.storage import expand
            tag = get_tag(tag_id)
            if tag:
                return expand(tag), 200
            else:
                return {}, 404
