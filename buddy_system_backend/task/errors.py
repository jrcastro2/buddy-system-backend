"""User errors."""
from buddy_system_backend.errors import RESTException


class TaskDoesNotExistError(RESTException):
    """Non-existent training."""

    code = 404
    """HTTP Status code."""

    def __init__(self, task=None, **kwargs):
        """Initialize exception."""
        super(RESTException, self).__init__(**kwargs)
        self.description = "Task{0}could not be resolved.".format(
            " #{0} ".format(task) if task else " "
        )
