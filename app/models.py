from app import db
from sqlalchemy import types

class ChatHistory(db.Model):
    __tablename__ = 'chat_history'

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(50))
    message = db.Column(db.Text)
    timestamp = db.Column(db.DateTime)

    def __repr__(self):
        return f'<ChatHistory {self.role} {self.timestamp}>'

class Document(db.Model):
    __tablename__ = 'documents'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    content = db.Column(types.Text, nullable=False)  # Using LONGTEXT from SQLAlchemy's types

    def __repr__(self):
        return f'<Document {self.name}>'

