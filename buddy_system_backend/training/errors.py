"""User errors."""
from buddy_system_backend.errors import RESTException


class TrainingDoesNotExistError(RESTException):
    """Non-existent training."""

    code = 404
    """HTTP Status code."""

    def __init__(self, training=None, **kwargs):
        """Initialize exception."""
        super(RESTException, self).__init__(**kwargs)
        self.description = "Training{0}could not be resolved.".format(
            " #{0} ".format(training) if training else " "
        )
