from sqlalchemy import type_coerce
from sqlalchemy.sql.schema import CheckConstraint
from sqlalchemy.types import SchemaType, TypeDecorator, SmallInteger


class EnumType(SchemaType, TypeDecorator):

    impl = SmallInteger

    def __init__(self, enum):
        self.enum = enum
        TypeDecorator.__init__(self)
        SchemaType.__init__(self)

    def copy(self):
        return EnumType(self.enum)

    def process_bind_param(self, value, dialect):
        if value is None:
            return None
        return int(value)

    def process_result_value(self, value, dialect):
        if value is None:
            return None
        return self.enum(value)

    def _set_table(self, column, table):
        e = CheckConstraint(type_coerce(column, self).in_(x.value for x in self.enum),
                            'valid_enum_{}'.format(column.name))
        assert e.table is table
