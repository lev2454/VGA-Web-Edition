import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class Group(SqlAlchemyBase):
    __tablename__ = 'groups'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    screen_name = sqlalchemy.Column(sqlalchemy.String)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    is_closed = sqlalchemy.Column(sqlalchemy.Boolean)
    deactivated = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    city = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    country = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    added_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)