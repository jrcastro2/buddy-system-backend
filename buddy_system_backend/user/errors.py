"""User errors."""
from buddy_system_backend.errors import RESTException


class UserDoesNotExistError(RESTException):
    """Non-existent user."""

    code = 404
    """HTTP Status code."""

    def __init__(self, user=None, **kwargs):
        """Initialize exception."""
        super(RESTException, self).__init__(**kwargs)
        self.description = "User{0}could not be resolved.".format(
            " #{0} ".format(user) if user else " "
        )


class InvalidPasswordError(RESTException):
    """Invalid Password."""

    code = 404
    """HTTP Status code."""

    def __init__(self, user=None, **kwargs):
        """Initialize exception."""
        super(RESTException, self).__init__(**kwargs)
        self.description = "Password validation failed for user{0}.".format(
            " #{0}".format(user) if user else " "
        )


class ConfirmationPasswordError(RESTException):
    """Confirmation of password failed ."""

    code = 404
    """HTTP Status code."""

    def __init__(self, **kwargs):
        """Initialize exception."""
        super(RESTException, self).__init__(**kwargs)
        self.description = "Password and confirmation password do not match."


class UserNotActivatedError(RESTException):
    """User is not activated."""

    code = 404
    """HTTP Status code."""

    def __init__(self, user=None, **kwargs):
        """Initialize exception."""
        super(RESTException, self).__init__(**kwargs)
        self.description = "User{0}not activated.".format(
            " #{0} ".format(user) if user else " "
        )


class UserNotAdminError(RESTException):
    """User is not admin."""

    code = 401
    """HTTP Status code."""

    def __init__(self, user=None, **kwargs):
        """Initialize exception."""
        super(RESTException, self).__init__(**kwargs)
        self.description = "User{0}is not admin.".format(
            " #{0} ".format(user) if user else " "
        )


class UserNotAuthenticatedError(RESTException):
    """User is not authenticated."""

    code = 401
    """HTTP Status code."""

    def __init__(self, user=None, **kwargs):
        """Initialize exception."""
        super(RESTException, self).__init__(**kwargs)
        self.description = "User{0}is not authenticated.".format(
            " #{0} ".format(user) if user else " "
        )
