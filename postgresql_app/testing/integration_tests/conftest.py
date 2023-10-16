import os
import subprocess
import time
from pathlib import Path

import pytest  # type: ignore # todo
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from postgresql_app.auxiliary import get_url
from postgresql_app.create_env_file import create_env_file


@pytest.fixture(scope="module")
def initialize_db():
    # change dir
    current_dir = os.getcwd()
    os.chdir("./postgresql_app")
    create_env_file(Path("."))
    #    subprocess.run("docker-compose -f docker-compose.yaml up --wait", shell=True)
    time.sleep(2)
    subprocess.run(["alembic", "upgrade", "head"], shell=True)
    engine = create_engine(get_url())
    session = sessionmaker(bind=engine)
    session = session()
    # Teardown: close session, stop and remove container
    yield session
    session.close()
    #    subprocess.run("docker-compose -f docker-compose.yaml down -v", shell=True)
    os.chdir(current_dir)
