"""User errors."""
from buddy_system_backend.errors import RESTException


class OnboardingDoesNotExistError(RESTException):
    """Non-existent training."""

    code = 404
    """HTTP Status code."""

    def __init__(self, onboarding=None, **kwargs):
        """Initialize exception."""
        super(RESTException, self).__init__(**kwargs)
        self.description = "Onboarding{0}could not be resolved.".format(
            " #{0} ".format(onboarding) if onboarding else " "
        )
