# gameMatcher
This repo is a student group project for the CS203 class (Yoobee Colleges, Auckland campus)

## Objectives

To create a web ~~app~~ project that effectively matches gamers with games. 

- [X] Users can take a gaming quiz
- [ ] System takes the user input and calculates the results for that user
- [ ] System uses the results to calculate game recommendations
- [ ] Users decide which games are/are not a match
- [ ] System learns from the users' choices and adjusts future predictions based on similar users (collaborative filtering)

## Frameworks/Libraries

- Django
- jQuery
- Bootstrap


# 1. Install gameMatcher

First of all clone this repo to your device:

`git clone https://github.com/maria-gedye/gameMatcher.git`


## 2. Create a virtual environment

Navigate inside the directory to gameMatcher/gmsite/
in the command line and use the following command to call the venv module:

`python -m venv env`

now activate the virtual environment:

`# Windows`

`source env/Scripts/activate`

`# Linux, WSL or macOS`

`source env/bin/activate`


## 3. Install packages

After creating a virtual environment(previous step), restore the project using:

`pip install -r requirements.txt`

check what packages have been installed:

`pip freeze`


## 4. Start the project

if you haven't already, navigate to the gmsite folder (cd gameMatcher/gmsite)

then run the server by using: 

`python manage.py runserver`

website should be displaying locally on [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

When you want to end your session or run another project, make sure you deactivate your virtual environment using the command:

`deactivate`



## Access the admin site

Make sure you have followed steps 1-3 and that the server is running:

`python manage.py runserver`

admin website should be displaying locally on [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

You should see a login page. This is the default admin login details:

Username: foo

Password: bar