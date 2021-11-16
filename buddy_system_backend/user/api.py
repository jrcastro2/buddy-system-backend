"""User api."""
from buddy_system_backend import User
from buddy_system_backend.user.errors import (
    UserDoesNotExistError,
    InvalidPasswordError,
    UserNotActivatedError,
)


def get_and_validate_user(user_dict):
    """Checks if user is valid and returns it."""
    user = User.query.filter_by(username=user_dict["username"]).first()
    if not user:
        raise UserDoesNotExistError(user_dict["username"])
    if not user.check_password(user_dict["password"]):
        raise InvalidPasswordError(user.id)
    if not user.is_active:
        raise UserNotActivatedError(user.id)

    return user
