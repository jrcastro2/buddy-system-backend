import json

from werkzeug.exceptions import HTTPException


class RESTException(HTTPException):
    """HTTP Exception delivering JSON error responses."""

    def __init__(self, errors=None, **kwargs):
        """Initialize RESTException."""
        super(RESTException, self).__init__(**kwargs)

    def get_description(self, environ=None, scope=None):
        """Get the description."""
        return self.description

    def get_body(self, environ=None, scope=None):
        """Get the request body."""
        body = dict(
            status=self.code,
            message=self.get_description(environ),
        )

        return json.dumps(body)

    def get_headers(self, environ=None, scope=None):
        """Get a list of headers."""
        return [("Content-Type", "application/json")]


class JSONSchemaValidationError(RESTException):
    """JSONSchema validation error exception."""

    code = 400

    def __init__(self, error=None, **kwargs):
        """Initialize exception."""
        super(RESTException, self).__init__(**kwargs)
        self.description = "Validation error: {0}.".format(
            error.messages if error else ""
        )
