# A django playground

Try things in this project

## Gettings Started

Virtual env

    python3.7 -m venv env
    source env/bin/activate

Install requirements

    pip install -r requirements.txt

Run it

    ./manage.py runserver

## Apps

### Waiting

* Demonstrate how a task queue can be used to do a long running task in a request response cycle.
* Ensure that an `Accepted 202` is returned immediately to the user, with a task id.
* Ensure that the task state can be queried by the user to see the status.
* Ensure errors encountered during task execution are logged

