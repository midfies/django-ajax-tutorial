"""Custom Exception for missing JSON data."""


class JsonNotFound(object):
    """Json not found exception."""

    def __init__(self):
        """Init a Json not found exception."""
        Exception.__init__(self, 'Record not found')
