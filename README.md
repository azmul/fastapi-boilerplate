## Create Python Env
python3 -m venv env

## Install dependencies
pip install fastapi uvicorn

## Run Server
uvicorn main:app --reload --port=8000 --host=0.0.0.0

## Create requirements.txt file
pip freeze > requiremnents.txt

## Deactivate the virtual environment
deactivate

## Docker Build
docker compose up --build

## Run Docker Image
docker compose up

