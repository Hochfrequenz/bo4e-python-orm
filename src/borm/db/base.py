"""
This module is mainly used by Alembic
It imports all database models to be able to create all related tables
"""

import importlib
import os

import src.borm.models  # noqa # pylint: disable=unused-import

# Import all the models, so that Base has them before being
# imported by Alembic, e.g. MappingBase will be imported by alembic (cf. db/*_db/migrations/env.py). This module is also
# imported by the create_db function.
from src.borm.db.base_class import MappingBase, mapper_registry  # noqa # pylint: disable=unused-import


def import_all_modules(package):  # type: ignore[no-untyped-def]
    """
    Import all modules from package
    Currently not used
    """
    modules = []
    package_path = os.path.dirname(package.__file__)

    for filename in os.listdir(package_path):
        if filename.endswith(".py") and not filename.startswith("__"):
            module_name = f"{package.__name__}.{filename[:-3]}"
            module = importlib.import_module(module_name)
            modules.append(module)

    return modules
