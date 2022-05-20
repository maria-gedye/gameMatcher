# gameMatcher
This repo is a student group project for the CS203 class (Yoobee Colleges, Auckland campus)

## Objective

To create a web ~~app~~ project that effectively matches gamers with games. 
1. Users take a gamer motivation test 
2. System takes their results as input into a recommendation system
3. Recommendation system predicts a list of games that match a user's 'gamer personality'
4. Users decide which games are/are not a match
5. System learns from the users' choices and adjusts future predictions based on similar users (collaborative filtering)

## Frameworks/Libraries

- Django
- jQuery


# Install gameMatcher

First of all clone this repo to your device:

`git clone https://github.com/maria-gedye/gameMatcher.git`


## Create a virtual environment

Navigate inside the directory to gameMatcher/gmsite/
in the command line and use the following command to call the venv module:

`python -m venv env`

now activate the virtual environment:

`# Windows`

`source env/Scripts/activate`

`# Linux, WSL or macOS`

`source env/bin/activate`


## Install packages

After creating a virtual environment(previous step), restore the project using:

`pip install -r requirements.txt`

check what packages have been installed:

`pip freeze`


## Start the project

if you haven't already, navigate to the gmsite folder (cd gameMatcher/gmsite)

then run the server by using: 

`python manage.py runserver`

website should be displaying locally on [http://localhost:8000/quiz/](http://localhost:8000/quiz/)

