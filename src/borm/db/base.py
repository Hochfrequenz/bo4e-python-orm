"""
This module is mainly used by Alembic
It imports all database models to be able to create all related tables
"""
import importlib
import os

import borm.models
import borm.models.many

# Import all the models, so that Base has them before being
# imported by Alembic
# from borm.db.base_class import Base, mapper_registry


def import_all_modules(package):
    modules = []
    package_path = os.path.dirname(package.__file__)

    for filename in os.listdir(package_path):
        if filename.endswith(".py") and not filename.startswith("__"):
            module_name = f"{package.__name__}.{filename[:-3]}"
            module = importlib.import_module(module_name)
            modules.append(module)

    return modules
