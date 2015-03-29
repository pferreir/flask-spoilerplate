import os
from contextlib import contextmanager

from flask_script import Manager
from geocashing.app import app


@contextmanager
def cd(path):
    """Context manager that changes CWD"""
    path = os.path.expanduser(path)
    old_path = os.getcwd()
    os.chdir(path)
    yield
    os.chdir(old_path)


manager = Manager(app)


@manager.command
def bower():
    """Installs all bower components and moves them to static/lib/*"""
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with cd(dir_path):
        os.system('bower install')


@manager.command
def createdb():
    """Creates an empty DB"""
    from geocashing.db import db

    db.create_all()
    db.session.commit()


if __name__ == "__main__":
    manager.run()
