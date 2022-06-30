import uuid
import datetime
from config import db
from sqlalchemy.dialects.postgresql import UUID


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    login = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=True, default=False)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __repr__(self):
        return f'<User {self.login}>'


class UserHistory(db.Model):
    __tablename = 'user_history'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    user_id = db.Column(UUID, db.ForeignKey('users.id'), index=True, nullable=False)
    user_name = db.Column(db.String, nullable=False)
    user_agent = db.Column(db.String, nullable=True)
    ip_address = db.Column(db.String, nullable=True)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow())
