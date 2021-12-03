from typing import Optional

from django.contrib.auth import authenticate

from leadsaveurs.users.models import User


def authenticate_user(username, password) -> Optional[User]:
    user = authenticate(username)
    if not user:
        return None
    valid_password = user.check_password(password)
    if valid_password:
        return user
    return None
