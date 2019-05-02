# A django playground

Try things in this project

## Gettings Started

Prerequisites:

* [RabbitMQ](https://www.rabbitmq.com/download.html) installed and running on your host

    brew update
    brew reinstall rabbitmq
    # Run as a service
    brew services start rabbitmq
    # Run ad-hoc
    rabbitmq-server
    
* The celery worker running from project root

    celery -A django_playground worker -l info

If you use just `celery worker` you will get the relative import error.

Virtual env

    python3.7 -m venv env
    source env/bin/activate

Install requirements

    pip install -r requirements.txt

Migrate the db

    ./manage.py migrate

Run it

    ./manage.py runserver

## Apps

### Waiting

* Demonstrate how a task queue can be used to do a long running task in a request response cycle.
* Ensure that an `Accepted 202` is returned immediately to the user, with a task id.
* Ensure that the task state can be queried by the user to see the status.
* Ensure errors encountered during task execution are logged
* Ensure the interval between those tasks is long - 20 seconds - to prevent double clicking issues

#### Monitoring Status

To list the active nodes in a cluster:

    celery -A { project_name } status
    celery -A django_playground status

Show the result of a task

    celery -A { project_name } result -t tasks.add 4e196aa4-0141-4601-8138-7aa33db0f577
    celery result 65d62b66-8609-474a-8fc3-b75815eaddb0
    celery -A django_playground result -t 65d62b66-8609-474a-8fc3-b75815eaddb0

Inspect active tasks

    celery  inspect active

But for production you would want to use [flow-er](http://docs.celeryproject.org/en/latest/userguide/monitoring.html#flower-real-time-celery-web-monitor)

Start it

    celery flower

View it

    open http://localhost:5555

View it on the curses (command line) monitor

    celery events

If you have not started any celery workers, the tasks will remain in the queue.

* Add a soft timeout
* Use a different task result backend
* Add an interval where only a single vdc per minute
