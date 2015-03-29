import flask_sqlalchemy

from geocashing.models.base import EnhancedModel

flask_sqlalchemy.Model = EnhancedModel

db = flask_sqlalchemy.SQLAlchemy()
