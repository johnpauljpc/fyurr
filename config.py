import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.

DEBUG = True

# Connect to the database


#  DATABASE URL IMPLEMENTED
SQLALCHEMY_DATABASE_URI = 'postgres://gzkfzewmalkkyw:5221e5f9e3c855c9692796fc5754d6c98d769498b3fab61543e4c8ebe31149fd@ec2-50-19-255-190.compute-1.amazonaws.com:5432/d63ubnjc9mmd9p'
SQLALCHEMY_TRACK_MODIFICATIONS = True