from flask_restplus import fields


def get_uuid_field(**kwargs):
    """Create a simple UUID field."""
    required = kwargs.pop('required', True)
    return fields.String(
        min_length=36,
        max_length=36,
        required=required,
        **kwargs)


def get_error_model(api, area):
    return api.model('%s_error' % area, {
        'message': fields.String(required=True,
                                 description='An explanation of the error.'),
    })
