# Awesome and automatic logging on Python

Robocorp's Python automation contains a gem for anyone working on Python and wants to efficiently log the execution, debug errors and monitor things in production. It's all open source, and with these simple instructions you'll be up and running in minutes, and get these beautiful logs for every run:


1. Install `robocorp-tasks` package from [PyPi](https://pypi.org/project/robocorp-tasks). Using virtual environments is of course recommended.

```py
pip install robocorp-tasks
```

```py
from robocorp.tasks import task
```

```py
python -m robocorp.tasks run <path/to/file.py or directory> -t <task_name>
```

```py
python -m robocorp.tasks run my-thing.py -t my_entry_point
```
