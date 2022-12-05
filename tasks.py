import os

from invoke import task

docker_username = "beverts312"


def get_project_root():
    return os.path.dirname(os.path.realpath(__file__))


def docker_build(c, dir, name):
    with c.cd(f"{get_project_root()}/{dir}"):
        c.run(f"docker build -t {docker_username}/{name} .")


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


@task(aliases=["dbase"])
def build_base_image(c):
    docker_build(c, "mlbase", "mlbase")


@task(aliases=["dml"])
def build_ml_image(c):
    docker_build(c, "pytorch", "machine-learning")


@task(aliases=["dsuper", "ds"])
def build_super_image(c):
    docker_build(c, "", "mlsuper")
