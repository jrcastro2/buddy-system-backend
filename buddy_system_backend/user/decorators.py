from functools import wraps

from flask_jwt_extended import current_user, jwt_required

from buddy_system_backend.user.errors import (
    UserNotAdminError,
    UserNotAuthenticatedError,
)


def is_admin(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_anonymous:
            raise UserNotAuthenticatedError()
        if not current_user.is_admin:
            raise UserNotAdminError(current_user.id)
        return f(*args, **kwargs)

    return decorated_function
