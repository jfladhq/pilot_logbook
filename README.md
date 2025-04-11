[![CodeQL](https://github.com/jfladhq/pilot_logbook/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/jfladhq/pilot_logbook/actions/workflows/codeql-analysis.yml)

# Pilot Logbook

Logbook to track pilot flying miles using FastAPI, SQLAlchemy, Alembic for backend and React for the frontend. I will be creating this using Docker files to be able to run everything just by running the 
docker.yml file. (Currently work in progress)

Will need to use my forked version of [FastAPI CRUDRouter](https://github.com/jfladhq/fastapi-crudrouter)

## Common commands you might have to use:
``` 
alembic revision --autogenerate -m "Description" -- Used to compare local model changes with database
alembic upgrade head -- Used to push model changes to database
alembic history
alembic downgrade -"Number of revisions"
alembic downgrade "Revision Number"
pipreqs --encoding=utf8 --force --ignore .venv

Install fastapi-crudrouter pre 2.0 SqlAlchemy
pip install git+https://github.com/jfladhq/fastapi-crudrouter.git@master
```
