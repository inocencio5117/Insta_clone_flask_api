import os
from config import db
from models import Profile

# Data to initialize database with
USER = [
    {
        "firstName": "Vinicius",
        "lastName": "Inocêncio",
        "age": 24,
        "bio": "This is my bio",
    }
]

# Delete database file if it exists currently
if os.path.exists("profile.db"):
    os.remove("profile.db")

# Create the database
db.create_all()

p = Profile(
    first_name=["lastName"],
    last_name=USER["firstName"],
    age=USER["age"],
    bio=USER["bio"],
)
db.session.add(p)

db.session.commit()
