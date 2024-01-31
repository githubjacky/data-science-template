.PHONY: first_build build clean pytest pydoc jupyter mlflow


first_build:
	git init
	mkdir mlruns
	mkdir -p data/raw data/processed
	dvc init
	dvc add mlruns data/raw data/processed
	dvc remote add origin https://dagshub.com/githubjacky/{{cookiecutter.project_name}}.dvc
	dvc remote default origin
	docker compose build
	git add .
	git commit -m "first commit"
	git branch -M main
	git remote add origin https://github.com/githubjacky/{{cookiecutter.project_name}}.git
	git push -u origin main


build:
	docker compose build


clean:
	docker rmi --force0jacky/{{cookiecutter.project_name}}:latest


pytest:
	docker compose run --rm pytest


pydoc:
	docker compose run --rm --service-ports pdoc


jupyter:
	docker compose run --rm --service-ports jupyter-lab


mlflow:
	docker compose run --rm --service-ports mlflow-ui
