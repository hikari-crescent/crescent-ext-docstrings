import nox


@nox.session
def flake8(session):
    session.install("flake8")
    session.run("flake8", "crescent")


@nox.session
def codespell(session):
    session.install("codespell")
    session.run("codespell", "crescent")


@nox.session
def mypy(session):
    session.install("poetry")
    session.run("poetry", "install")
    session.run("mypy", "crescent")


@nox.session
def isort(session):
    session.install("isort")
    session.run("isort", "--check", "crescent")
