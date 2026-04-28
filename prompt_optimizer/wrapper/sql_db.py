import os
import sqlite3
from typing import Optional, Tuple


class SQLDBManager:
    """
    A class to manage an SQLite database.

    Attributes:
        database_name: The name of the SQLite database file.
        connection: The database connection object.
        cursor: The database cursor object.
    """

    def __init__(
        self, project_name: str = "default_project", database_path: Optional[str] = None
    ):
        """
        Initializes a new SQLDBManager object.

        Args:
            project_name: The name of the project.
            database_path: The path to the SQLite database file.
        """
        if database_path is None:
            home_dir = os.path.expanduser("~")
            database_dir = os.path.join(home_dir, ".prompt_optim")
            os.makedirs(database_dir, exist_ok=True)
            self.database_path = os.path.join(database_dir, "default.db")
        else:
            self.database_path = database_path

        self.connection = None
        self.cursor = None
        self.project_name = project_name
        self.table_name = self.project_name
        self.username = "default"

    def set_user(self, username):
        pass

    def __enter__(self):
        """
        Establishes the database connection and cursor when entering the context.
        """
        self.connect()
        self.create_table()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Closes the database connection and cursor when exiting the context.
        """
        self.close()

    def connect(self):
        """
        Connects to the SQLite database.
        """
        pass

    def create_table(self):
        """
        Creates a table in the database if it doesn't exist.

        Args:
            table_name: The name of the table.
        """
        pass

    def add(self, data: Tuple) -> bool:
        """
        Adds data to the specified table.

        Args:
            data: A tuple containing the data to be added.

        Returns:
            bool: `True` if successfully inserted values else `False`.
        """
        pass

    def close(self):
        """
        Closes the database connection and cursor.
        """
        pass
