from . import _db


def setup(app):
    _db.setup(app)
    # import those packages that need db
    from . import user

    user.setup()
