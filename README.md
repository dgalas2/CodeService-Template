# Singlestore CodeService Template
To get started with this template, you will first need to install poetry.

You can use the [official guide](https://python-poetry.org/docs/) for steps on installing poetry.

## Project Structure
```
s2-codeservice-template
│   s2config.json
│
└───s2_codeservice_template
    │   __init__.py
    |   singleton.py
    │   database.py
    |   pyproject.toml
    │   poetry.lock
    |   .env.example
    |
    └───tests
        |   __init__.py
```

1. ` __init__.py` holds the entry point functions.
2. `database.py` has db connection class and db methods.
3. `singleton.py` allows db class to be used as singleton.
4. `pyproject.toml` is poetry config file.
5. `.env.example` should be used as a template for `.env` files

## Setting up project
1. Go to project folder
```
cd ./s2_codeservice_template
```
2. Install dependencies using poetry
```
poetry install
```
3. Run poetry script to start up project
```
poetry run my-app
```

## S2Config File
The configuration file is necessary for Helios platform to understand how to run yur project.
```
{
	"project_name":"s2-codeservice-template",
	"author":"S2DefaultAuthorName",
	"version":"1.0.0",
	"python_version":"^3.11",
	"entry_point":"my-app,
	"app":"CodeService",
	"readme":"./s2-codeservice-template/README.md",
	"poetryFile":"./s2-codeservice-template/pyproject.toml",
	"test":"./s2-codeservice-template/tests",
	"poetry":true,
	"database": "db1"
}
```
1. `entry_point` defines the poetry script that will be run when project is deployed.
2. `app` defines the type of nova app that you want your project to run as. Currently `app` should take values: `CodeService`, `Dashboard`, `ScheduledJob`
3. `database` defines your database name that your project connects to.

Remember to change these if you decide to rename the project.

## Enviornment file
The `.env.example` file defines how you should structure your enviornment file for [S2 python SDK](https://singlestoredb-python.labs.singlestore.com/).
```
# define your enviornment
# your enviornment specific variables (BASE_URL, LISTEN_PORT, BASE_PATH) should start with the name of the enviornment. 
# CONVENTION: <ENV>_<VARIABLE_NAME>, if ENV is not set to anything then first _ is not required
ENV=LOCAL_DEV


#define where the app will listen

#ENV:LOCAL_DEV
LOCAL_DEV_BASE_URL=http://127.0.0.1
LOCAL_DEV_LISTEN_PORT=5678
LOCAL_DEV_BASE_PATH="/"
# database connection details for local dev
LOCAL_DEV_DATABSE_NAME=db1
LOCAL_DEV_DB_USER_NAME=admin
LOCAL_DEV_DML_HOST="172.18.0.3" #dml host
LOCAL_DEV_DML_PORT=30736
LOCAL_DEV_DB_PASSWORD="my-databse-password"

#ENV:LOCAL_TEST
LOCAL_TEST_BASE_URL=http://127.0.0.1
LOCAL_TEST_LISTEN_PORT=8907
LOCAL_TEST_BASE_PATH="/"
```

The convention for naming app and DB specific variables i.e.
1. `BASE_URL`
2. `LISTEN_PORT`
3. `BASE_PATH`
4. `DATABSE_NAME`
5. `DB_USER_NAME`
6. `DB_PASSWORD`
6. `DML_HOST`
7. `DML_PORT`

should be `<ENV NAME>_<VARIABLE_NAME>`. 
