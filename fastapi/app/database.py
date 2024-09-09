"""Database connection and User model module.

This module sets up a MySQL database connection using environment variables
and defines a User model using Peewee ORM.
"""

import os
from dotenv import load_dotenv
from peewee import *

# Load environment variables
load_dotenv()

# Set up database connection
database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    passwd=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT")),
)


class UserModel(Model):
    """Represent a user in the system.

    This model defines the structure and attributes of a user entity
    using Peewee ORM.

    Attributes:
        id (AutoField): Unique identifier for the user (primary key).
        username (CharField): The username of the user (max length 50).
        email (CharField): The email address of the user (max length 50).
        password (CharField): The password for the user's account (max length 50).
    """

    id = AutoField(primary_key=True)
    username = CharField(max_length=50)
    email = CharField(max_length=50)
    password = CharField(max_length=50)

    class Meta:
        """
        Meta class for defining database configurations.

        Attributes:
            database: The database connection instance.
            table_name (str): The name of the table in the database.
        """

        database = database
        table_name = "users"
