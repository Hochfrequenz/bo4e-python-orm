# Python BO4E ORM


![Unittests status badge](https://github.com/Hochfrequenz/bo4e-python-orm/workflows/tests/badge.svg)
![Coverage status badge](https://github.com/Hochfrequenz/bo4e-python-orm/workflows/Coverage/badge.svg)
![Linting status badge](https://github.com/Hochfrequenz/bo4e-python-orm/workflows/Linting/badge.svg)
![Black status badge](https://github.com/Hochfrequenz/bo4e-python-orm/workflows/Formatting/badge.svg)

At this point this repository serves only as a exemplary implementation of a BO4E ORM. The main work (i.e. the generation of SQL Model code) will be done in the [BO4E-CLI-Tool](https://github.com/bo4e/BO4E-CLI)


A ORM tool to map between SQL databases and BO4E classes using:
- SQLModel (https://sqlmodel.tiangolo.com) for the ORM
- BO4E-Schema-Tool (https://pypi.org/project/BO4E-Schema-Tool) to pull and modify an existing BO4E version
- BO4E-Python-Generator (https://pypi.org/project/BO4E-Python-Generator) to generate SQLModel classes from the BO4E schema
- Docker Container (https://www.docker.com) to create the database with
- PostgreSQL (https://www.postgresql.org)
  (- In principle, Alembic (https://alembic.sqlalchemy.org) is supported for migrations, but not further supported at the moment)

The idea of this tool is to provide a first instance of an ORM which has been generated from a specific BO4E version. For further information of the functionalities of this ORM framework, please refer to the documentation of [SQLModel](https://sqlmodel.tiangolo.com).
Please note that this is a very early version of the ORM and might not be fully functional yet.

### Installation

It will also be [available on pypi](https://pypi.org/project/borm/).
```bash
pip install borm
```

### Description

To setup a test db (postgresql) run the following in your tox env (see below):
```bash
tox -e setup_testpostgresql
```
Make sure that your local host is running.

Alternatively, an existing bo4e version can be pulled via:
```bash
tox -e init_bo4e
```
This uses two other tools:
https://github.com/bo4e/BO4E-Schema-Tool
and
https://github.com/bo4e/BO4E-Python-Generator

Make sure you specify the version in tox.ini via the -t flag.

The fast way is to use:
```bash
tox -e setup_bo4e
```
which combines the steps above.

Enter the following to delete the test db:
```bash
tox -e remove_testpostgresql
```
In order to get a better understanding how this ORM works, you might want to have a look at the tests in the tests folder.

In principle, alembic migrations are supported, e.g. by running:
```bash
tox -e migration
```
However, this is not further supported at the moment.


## Contribute

You are very welcome to contribute to this repository by opening a pull request against the main branch.
If you use a windows OS you might need to change `psycopg` -> `psycopg[binary]` in the requirements.
