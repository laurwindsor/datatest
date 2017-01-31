import os

import config
from raven.contrib.flask import Sentry

from {{cookiecutter.app_name}}.app import create_app_singletons


def main():
    """Serve traffic."""
    config.init('{{ cookiecutter.app_name }}')

    app, api = create_app_singletons()

    Sentry(app, dsn=config.get('sentry.dsn'))

    app.run(
        debug=True if os.environ.get('DEBUG') else False,
        port=int(os.environ.get('PORT', 80)),
        host=os.environ.get('HOST', '0.0.0.0'))
