# flask-docker-example

Example of running Flask inside a docker container

## Directory layout

```
├── Dockerfile            --> docker build file
├── .dockerignore         --> file that must be ignored by the docker build process
├── .editorconfig         --> editor config file for formatting
├── .gitignore            --> file that need to be ignored by git
├── LICENSE               --> LICENSE file
├── Makefile              --> GNU Make file for automating commands
├── README.md             --> this file
├── env-config            --> configuration file directory
│ └── config.py           --> config file
├── flask_example         --> our main python package
│ ├── __init__.py         --> python flask package app init file where the magic happens
│ └── views               --> directory for all view classes
│     ├── __init__.py     --> python package init file ( this one is empty )
│     └── hello_world.py  --> view handler file ( currently holding 2 views classes )
├── manage.py             --> manage file for executing and starting the flask API
└── requirements.txt      --> Python pip dependencies file
```

## Available Configuration settings

| Name | Default value | Description |
|:----:|:-------------:|:------------|
|API_PORT|8080|the default port to run on|
|LOG_LEVEL|INFO|the log level to use, can be INFO,ERROR,DEBUG|
|WORKERS|4| the worker threads to spawn for running the application|

## Dev Requirements

* Linux or MacOS
* Python 3.7.9 or higher
* Make
* Python virtualenv

### create dev environment

```
make dev/deps
```

# Container building

build plain

```
make image/build
```

test plain build

```
make image/test
```

build and push to custom repo

```
export IMAGE_REPO="somerepo-uri"
docker login $IMAGE_REPO
make image/push
```
