SimpleAPI server

SimpleAPI -- a simple flask-based API server designed to demonstrate unit testing, the use of Postman, and automated testing in as part of the GitLab CI/CD pipeline

## Install requirements

It is highly recommended to make use of a virtual environment to prevent conflicts with other requirements.

Be sure you have pip3 installed already (sudo apt install python3-pip)

pip3 install -r requirements.txt

## Run SimpleAPI server:

python3 app/server.py

## Run Tests

python3 -m pytest
