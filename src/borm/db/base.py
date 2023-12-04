"""
This module is mainly used by Alembic
It imports all database models to be able to create all related tables
"""

# Import all the models, so that Base has them before being
# imported by Alembic
from borm.db.base_class import MappingBase, mapper_registry
