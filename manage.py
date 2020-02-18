#!/usr/bin/python
# Author: Brad Sickler
# Description: A boilerplate for a super simple REST API implementation
# Derived from: https://www.freecodecamp.org/news/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563/#project-setup-and-organization

import os
import unittest
# from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager  # , Command, Option
from app import application

# The manager handles command line options in this case
manager = Manager(application)

HOST = "127.0.0.1"
PORT = 10028

# migrate = Migrate(app, db)
# manager.add_command('db', MigrateCommand)

@manager.command
def run():
    application.run(host=HOST, port=PORT)


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
