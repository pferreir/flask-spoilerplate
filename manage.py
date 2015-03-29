import os

from flask_script import Manager
from geocashing.app import app


class cd:
    """Context manager that changes CWD"""
    def __init__(self, new_path):
        self.new_path = os.path.expanduser(new_path)

    def __enter__(self):
        self.saved_path = os.getcwd()
        os.chdir(self.new_path)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.saved_path)

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
