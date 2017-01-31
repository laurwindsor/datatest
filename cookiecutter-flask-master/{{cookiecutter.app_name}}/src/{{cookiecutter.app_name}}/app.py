from flask import Flask
from flask_restplus import Api

import {{cookiecutter.app_name}}.views.health
import {{cookiecutter.app_name}}.views.tags


def create_app_singletons():
    app = Flask('{{cookiecutter.app_name}}')
    api = Api(app, title='{{cookiecutter.app_name}}',
              description="""Do things related to {{cookiecutter.app_name}}!""")

    {{cookiecutter.app_name}}.views.tags.init_app(app, api)
    {{cookiecutter.app_name}}.views.health.init_app(app, api)

    return app, api
