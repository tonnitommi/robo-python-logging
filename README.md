# Awesome and automatic logging on Python

Robocorp's Python automation contains a gem for anyone working on Python and wants to efficiently log the execution, debug errors and monitor things in production. It's all open source, and with these simple instructions you'll be up and running in minutes, and get these beautiful logs for every run:


Install `robocorp-tasks` package from [PyPi](https://pypi.org/project/robocorp-tasks). Using virtual environments is of course recommended.

```py
pip install robocorp-tasks
```

In your Python project, import the task decorator.

```py
from robocorp.tasks import task
```

Then decorate your entry point with `@task`.

```py
@task
def my_entry_point():
    # do something
```

When running the code, use the following command instead of just the simple python + file command.

```bash
python -m robocorp.tasks run <path/to/file.py or directory> -t <task_name>
```

For example the entry point in this example would be run with:

```bash
python -m robocorp.tasks run my-thing.py -t my_entry_point
```

After the run, you'll always find the updated [log file in output folder](/output/log.html).

Voila! To learn more, check out the [robo](https://github.com/robocorp/robo/tree/master/tasks) repository.