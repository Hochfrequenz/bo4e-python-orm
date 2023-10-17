"""
This module is mainly used by Alembic
It imports all database models to be able to create all related tables
"""

# Import all the models, so that Base has them before being
# imported by Alembic
from db.base_class import Base, mapper_registry  # pylint: disable=unused-import

from src.models.bo.geschaeftspartner import Geschaeftspartner  # pylint: disable=unused-import
from src.models.com.adresse import Adresse  # pylint: disable=unused-import
