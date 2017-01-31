from __future__ import with_statement
import os
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = None

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def get_db_url():
    """Get the URL for the database."""
    return 'postgresql://%s:%s@%s:%d/%s' % (
        os.environ.get('RDS_USERNAME', os.environ['POSTGRES_USER']),
        os.environ.get('RDS_PASSWORD', os.environ['PGPASSWORD']),
        os.environ.get('RDS_HOSTNAME', os.environ['POSTGRES_HOST']),
        os.environ.get('RDS_PORT', 5432),
        os.environ.get('RDS_DB_NAME', '{{cookiecutter.app_name}}'),
    )


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = get_db_url()

    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    db_config = {
        'sqlalchemy.url': get_db_url(),
        'sqlalchemy.pool_recycle': '50',
        'sqlalchemy.echo': 'true'
    }

    connectable = engine_from_config(
        db_config,
        prefix='sqlalchemy.',
        poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
