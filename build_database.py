import os
from config import db, app
from models import Profile

with app.app_context():
    # Data to initialize database with
    USER = {
        "firstName": "Vinicius",
        "lastName": "Inocêncio",
        "age": 24,
        "bio": "This is my bio",
    }

    # Delete database file if it exists currently
    if os.path.exists("profile.db"):
        os.remove("profile.db")

    # Create the database
    db.create_all()

    p = Profile(
        first_name=USER["firstName"],
        last_name=USER["lastName"],
        age=USER["age"],
        bio=USER["bio"],
    )
    db.session.add(p)

    db.session.commit()
