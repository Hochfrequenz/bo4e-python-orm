"""
Auxiliary module to load url from env file
"""

import os

from dotenv import load_dotenv


def get_url() -> str:
    """
    Build the database connection URL based on the environment variables in .env
    """
    load_dotenv()
    user = os.getenv("MYSQL_USER")
    password = os.getenv("MYSQL_PASSWORD")
    server = os.getenv("MYSQL_SERVER")
    port = os.getenv("MYSQL_PORT")
    db = os.getenv("MYSQL_DB")
    if user is None and password is None and server is None and db is None and port is None:
        raise IOError("Could not load .env file.")
    if user is None or password is None or server is None or db is None or port is None:
        raise KeyError(
            f"Couldn't find all environment variables:\n"
            f"\tuser: '{user}'\n"
            f"\tpassword: '{password}'\n"
            f"\tserver: '{server}'\n"
            f"\tport: '{port}'\n"
            f"\tdb: '{db}'"
        )
    return f"mysql+pymysql://{user}:{password}@{server}:{port}/{db}"
