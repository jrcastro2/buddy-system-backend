"""User errors."""
from buddy_system_backend.errors import RESTException


class RoleDoesNotExistError(RESTException):
    """Non-existent training."""

    code = 404
    """HTTP Status code."""

    def __init__(self, role=None, **kwargs):
        """Initialize exception."""
        super(RESTException, self).__init__(**kwargs)
        self.description = "Role{0}could not be resolved.".format(
            " #{0} ".format(role) if role else " "
        )
