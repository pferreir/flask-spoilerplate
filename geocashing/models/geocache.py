from datetime import datetime
from enum import Enum

from geocashing.db import db
from geocashing.util.sqlalchemy import EnumType


class GeoCacheStatus(int, Enum):
    added = 1
    confirmed = 2
    needs_maintenance = 3
    dead = 4
    unknown = 5


class GeoCache(db.Model):
    __tablename__ = 'geocaches'

    id = db.Column('id', db.Integer, primary_key=True)
    code = db.Column(db.String(9), nullable=False, unique=True)
    title = db.Column(db.String(60), nullable=False)
    text = db.Column(db.String)
    state = db.Column(EnumType(GeoCacheStatus), nullable=False)
    creation_dt = db.Column(db.DateTime, nullable=False)

    def __init__(self, code, title, text=None):
        self.code = code
        self.title = title
        self.state = GeoCacheStatus.added
        self.text = text
        self.creation_dt = datetime.utcnow()
