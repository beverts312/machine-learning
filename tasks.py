import os

from invoke import task


def get_project_root():
    return os.path.dirname(os.path.realpath(__file__))


def black(c, check):
    cmd = f"black . --line-length=79 {'--check' if check is True else ''}"
    return c.run(cmd)


@task(aliases=["f"])
def format(c):
    project_root = get_project_root()
    with c.cd(project_root):
        c.run("isort .")
        black(c, False)


@task(aliases=["cf", "fc"])
def check_format(c):
    return black(c, True)
