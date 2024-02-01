# Flask-MicroBLog
Creating an Micro Blog with Flask and SQLAlchemy

## Setting Up the enviroment
First Create your venv
- $ python3 -m venv venv
Install the dependencies
- $ pip3 install -r requirements.txt

## Intiate the application
create the enviroment FLASK_APP variable, the .flaskenv do this for you with python-dotenv installed but if not you can do the command
- $ export FLASK_APP=microblog.py

## Start the application
need the enviroment variable created before
- $ flask run