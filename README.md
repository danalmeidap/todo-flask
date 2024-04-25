<h1 align="center">ToDo List</h1>
<p align="center">Application for scheduling task, using CLI or FORMS</p>
<p>This  application uses:</p>
<ul>
    <li> <a href="https://www.python.org/downloads/release/python-3810/">Python</a></li>
    <li> <a href="https://docs.python.org/3/library/typing.html">Type hints</a></li>
    <li> <a href="https://black.readthedocs.io/en/stable/">Black</a></li>
    <li> <a href="https://flask.palletsprojects.com/en/3.0.x/">Flask</a></li>
    <li> <a href="https://pymongo.readthedocs.io/en/stable/">FLASK-PYMONGO</a></li>
    <li> <a href="https://www.mongodb.com/languages/python/pymongo-tutorial">MONGODB</a></li>
</ul>

#

## Features
- [x] Add a task 
- [x] Lists tasks 
- [x] Get task by id
- [x] Get tasks by user
- [x] Add, list, update and delete a task using cli
- [x] Only authenticated users can add tasks

## How to use

### Clone or download repository and use docker to build Dockerfile

    '''docker build -t tasks .'''

### Run the docker-compose.yml using

    '''docker-compose up -d'''

### Go to app folder and uses for localhost operations

    '''flask run --debug''''

### To use cli command bellow and will shows the operations
    '''flask tasks'''