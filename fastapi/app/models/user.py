"""user model module.

This module defines the User model using Pydantic for data validation.
"""

from pydantic import BaseModel


class User(BaseModel):
    """Represent a user in the system.

    This model defines the structure and attributes of a user entity.

    Attributes:
        id (int): Unique identifier for the user.
        username (str): The username of the user.
        email (str): The email address of the user.
        password (str): The password for the user's account.
    """

    id: int
    username: str
    email: str
    password: str
