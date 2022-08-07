import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.

DEBUG = True

# Connect to the database


#  DATABASE URL IMPLEMENTED
SQLALCHEMY_DATABASE_URI = 'postgres://guxluloxutmqlr:3b93bd942aa652658291c0bea501a271d75224c9d4a0cc96172e75cf8a267979@ec2-34-235-198-25.compute-1.amazonaws.com:5432/d2adjsjdrv8np1'
SQLALCHEMY_TRACK_MODIFICATIONS = True