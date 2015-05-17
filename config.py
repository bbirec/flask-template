import os
"""
	Flask config variables based on configurations.
"""

class Config(object):
	DEBUG = False
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgres://localhost/bbirec')
