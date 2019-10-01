def validate_empty(field, name=None):
    if not field:
        raise ValueError('This field is Required.')
    if name and not field:
        raise validate_empty('{} is Required'.format(name))
