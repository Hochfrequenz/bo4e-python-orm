"""
This python script copies the env.example to .env if .env does not already exists.
This is similar to the bash command `mv example.env .env`.
It is used in all tox environments except the linting environment.
"""
from pathlib import Path
from shutil import copyfile

from borm.logger import logger


def create_env_file(directory_path: Path) -> None:
    """
    Checks if a file with the file name `destination_file_name` exists.
    If yes, nothing will be done.
    If not, it will copy the `source_file_name` file to the `destination_file_name` in the same directory.
    """
    source_file_name: str = ".env.example"
    destination_file_name: str = ".env"

    path_to_env_file: Path = directory_path / destination_file_name

    if path_to_env_file.exists():
        logger.info("✅ Great, you have already an environment file.")
    else:
        logger.info(
            "🤔 Uh I see you have no %s file in %s\n"
            "😊 But do not worry, I have you covered, I try to copy for you the %s file to %s",
            destination_file_name,
            directory_path,
            source_file_name,
            destination_file_name,
        )

        try:
            copyfile(directory_path / source_file_name, path_to_env_file)
            logger.info("🤗 And we are done.\nPlease update some credentials for your need, e.g. database credentials.")
        except FileNotFoundError:
            logger.info(
                "😞 I am so sorry, but the %s file is gone. Please ask someone of you colleagues to help you.",
                source_file_name,
            )


if __name__ == "__main__":
    root_directory_path = Path.cwd() / Path("borm/db/mysql_db")
    create_env_file(directory_path=root_directory_path)
