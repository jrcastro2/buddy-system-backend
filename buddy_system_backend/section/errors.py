"""User errors."""
from buddy_system_backend.errors import RESTException


class SectionDoesNotExistError(RESTException):
    """Non-existent training."""

    code = 404
    """HTTP Status code."""

    def __init__(self, section=None, **kwargs):
        """Initialize exception."""
        super(RESTException, self).__init__(**kwargs)
        self.description = "Section{0}could not be resolved.".format(
            " #{0} ".format(section) if section else " "
        )
