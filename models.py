from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Model for pet table"""
    __tablename__ = 'pets'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    name = db.Column(
        db.String,
        nullable=False
    )

    species = db.Column(
        db.String,
        nullable=False
    )

    img_url = db.Column(
        db.String,
        nullable=True
    )

    age = db.Column(
        db.Integer,
        nullable=True
    )

    notes = db.Column(
        db.String,
        nullable=True
    )

    available = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )
