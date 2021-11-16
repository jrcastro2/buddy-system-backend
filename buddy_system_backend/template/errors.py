"""User errors."""
from buddy_system_backend.errors import RESTException


class TemplateDoesNotExistError(RESTException):
    """Non-existent training."""

    code = 404
    """HTTP Status code."""

    def __init__(self, template=None, **kwargs):
        """Initialize exception."""
        super(RESTException, self).__init__(**kwargs)
        self.description = "Template{0}could not be resolved.".format(
            " #{0} ".format(template) if template else " "
        )
