from datetime import datetime
from config import db, ma


class Profile(db.Model):
    __tablename__ = "profile"
    profile_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(32), index=True)
    last_name = db.Column(db.String(100))
    bio = db.Column(db.String(255))
    age = db.Column(db.Integer)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class PersonSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Profile
        load_instance = True

    first_name = ma.auto_field()
    last_name = ma.auto_field()
    bio = ma.auto_field()
    age = ma.auto_field()
    profile_id = ma.auto_field()
