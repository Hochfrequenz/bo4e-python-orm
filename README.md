# Python BO4E ORM


![Unittests status badge](https://github.com/Hochfrequenz/bo4e-python-orm/workflows/tests/badge.svg)
![Coverage status badge](https://github.com/Hochfrequenz/bo4e-python-orm/workflows/Coverage/badge.svg)
![Linting status badge](https://github.com/Hochfrequenz/bo4e-python-orm/workflows/Linting/badge.svg)
![Black status badge](https://github.com/Hochfrequenz/bo4e-python-orm/workflows/Formatting/badge.svg)

A ORM tool to map between SQL databases and BO4E classes using:
...

### Installation

It will also be [available on pypi](https://pypi.org/project/borm/).
```bash
pip install borm
```

### Documentation

To setup a test db (postgresql) run the following in your tox env (see below):
```bash
tox -e setup_testpostgresql
```
Make sure that your local host is running.

Second, the alembic migration is done running:
```bash
tox -e migration
```
Enter the following to delete the test db:
```bash
tox -e remove_testpostgresql
```


## How to use this Repository on Your Machine

Follow the instructions in our [Python template repository](https://github.com/Hochfrequenz/python_template_repository#how-to-use-this-repository-on-your-machine).

## Contribute

You are very welcome to contribute to this repository by opening a pull request against the main branch.
If you use a windows OS you might need to change psycopg -> psycopg[binary] in the requirements.
