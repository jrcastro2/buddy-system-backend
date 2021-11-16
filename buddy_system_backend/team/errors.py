"""User errors."""
from buddy_system_backend.errors import RESTException


class TeamDoesNotExistError(RESTException):
    """Non-existent training."""

    code = 404
    """HTTP Status code."""

    def __init__(self, team=None, **kwargs):
        """Initialize exception."""
        super(RESTException, self).__init__(**kwargs)
        self.description = "Team{0}could not be resolved.".format(
            " #{0} ".format(team) if team else " "
        )
