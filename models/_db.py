from flask_mongoengine import MongoEngine

DB = None


def setup(app):
    global DB
    DB = MongoEngine(app)
