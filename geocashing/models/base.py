from flask_sqlalchemy import Model
from sqlalchemy.orm import class_mapper, ColumnProperty


class EnhancedModel(Model):
    """Model class that includes some util methods"""

    @classmethod
    def _get_column_attrs(cls):
        return {prop.key for prop in class_mapper(cls).iterate_properties if isinstance(prop, ColumnProperty)}

    @classmethod
    def find(cls, *args, **kwargs):
        column_attrs = cls._get_column_attrs()
        invalid_args = {arg for arg in kwargs if arg not in column_attrs}
        if invalid_args:
            raise ValueError('Invalid_args: {}'.format(invalid_args))

        return cls.query.filter_by(**kwargs).filter(*args)

    @classmethod
    def find_all(cls, *args, **kwargs):
        return cls.find(*args, **kwargs).all()

    @classmethod
    def find_first(cls, *args, **kwargs):
        return cls.find(*args, **kwargs).first()

    @classmethod
    def find_one(cls, *args, **kwargs):
        return cls.find(*args, **kwargs).one()

    @classmethod
    def get(cls, oid):
        return cls.query.get(oid)
