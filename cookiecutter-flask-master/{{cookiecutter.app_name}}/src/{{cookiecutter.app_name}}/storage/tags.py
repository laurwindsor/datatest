import json

from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequest

from doh import put_item, get_item

TAG_TABLE = 'tag'


def get_tag_fields():
    """The list of fields in the DB."""
    return [
        'id',
        'timestamp',
        'created_by',
        'name',
        'description',
        'client_data',
        'expiry_seconds',
        'public',
    ]


def get_tag(tag_id, timestamp=None):
    """Lookup a Tag from the database."""
    return get_item(tag_id, TAG_TABLE, get_tag_fields(), timestamp=timestamp)


def put_tag(tag):
    """Place a tag item into the database."""
    tag = tag.copy()
    tag.setdefault('created_by', None)
    # Make sure the JSON field 'localizations' is serializeable
    tag['localizations'] = json.dumps(tag.get('localizations', []))
    try:
        return put_item(tag, TAG_TABLE, get_tag_fields())
    except IntegrityError as e:
        raise BadRequest('Integrity error %s in request. Please try again.' %
                         str(e))


def tag_match(tag, search):
    if not tag:
        return False

    # Check the name
    name = tag.get('name') or ''
    if search.lower() in name.lower():
        return True

    # Check the description
    description = tag.get('description') or ''
    if search.lower() in description.lower():
        return True

    # Check the description
    client_data = tag.get('client_data') or ''
    if search.lower() in client_data.lower():
        return True
