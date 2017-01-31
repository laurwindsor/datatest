import doh


def get_tables():
    """Get this app's tables."""
    return []


doh.init(db_url=doh.get_db_url('{{cookiecutter.app_name}}'))
