import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.

DEBUG = True

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
# Connect to the database

#SQLALC
#  DATABASE URL IMPLEMENTED
#SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:07061651502@localhost:5432/fyyur'
SQLALCHEMY_TRACK_MODIFICATIONS = True