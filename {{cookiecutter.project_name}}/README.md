# {{cookiecutter.project_name}}
*{{cookiecutter.description}}*


## Tools used in this project
- [docker](https://www.docker.com/): runtime environment
- [Poetry](https://python-poetry.org/docs/#installation): package management
* [hydra](https://hydra.cc/): Manage configuration files
* [DVC](https://dvc.org/): Data version control
* [sphinx](https://www.sphinx-doc.org/en/master/): Automatically create an API documentation for your project
- [mlflow](https://mlflow.org/#core-concepts): experiment tracking


## Set up the environment, and Install dependencies
1. Install docker
2. create the docker image:
```bash
make build
```
To clean up the docker image:
```sh
make clean
```


## Container Services
```sh
# unit test
make pytest

# project documentation
make pydoc

# development IDE - Jupyter Lab
make jupyter

# MLflow tracking UI
make mlflow
```


## process scripts/notebooks
