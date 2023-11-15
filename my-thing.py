from robocorp.tasks import task

@task
def my_entry_point():
    variable = 0
    for x in (1, 3, 7):
        variable += x
    print(f"Hello Robo and {variable}!")