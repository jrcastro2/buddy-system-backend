"""User errors."""
from buddy_system_backend.errors import RESTException


class ModuleDoesNotExistError(RESTException):
    """Non-existent training."""

    code = 404
    """HTTP Status code."""

    def __init__(self, module=None, **kwargs):
        """Initialize exception."""
        super(RESTException, self).__init__(**kwargs)
        self.description = "Module{0}could not be resolved.".format(
            " #{0} ".format(module) if module else " "
        )
