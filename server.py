from flask import render_template, request, abort
from config import app, db
from models import Profile, ProfileSchema


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/health_check")
def health_check():
    return "This route is healthy "


@app.route("/profile/all", methods=["GET"])
def read_all():
    profiles = Profile.query.order_by(Profile.first_name).all()

    profile_schema = ProfileSchema(many=True)
    return profile_schema.dump(profiles)


@app.route("/profile/<profile_id>", methods=["GET"])
def read_one(profile_id):
    """Endpoint documentation
    ---
    parameters:
      - name: profile_id
        in: path
        type: integer
        required: true
    definitions:
      Profile:
        type: object
        properties:
          first_name:
            type: string
          last_name:
            type: string
          bio:
            type: string
          age:
            type: integer
            format: int32
    responses:
      200:
        description: The profile that has been searched
        schema:
          $ref: '#/definitions/Profile'
    """
    profile = Profile.query.filter(Profile.profile_id == profile_id).one_or_none()

    if profile is not None:
        profile_schema = ProfileSchema()
        return profile_schema.dump(profile)
    else:
        abort(404, f"Profile not found for id: {profile_id}")


@app.route("/profile", methods=["POST"])
def create_profile():
    profile = request.get_json()
    print(profile)
    first_name = profile["first_name"]
    last_name = profile["last_name"]

    existing_profile = (
        Profile.query.filter(Profile.last_name == last_name)
        .filter(Profile.first_name == first_name)
        .one_or_none()
    )

    if existing_profile is None:
        schema = ProfileSchema()
        new_profile = schema.load(profile, session=db.session)

        db.session.add(new_profile)
        db.session.commit()

        return schema.dump(new_profile), 201
    else:
        abort(409, f"Profile {first_name} {last_name} exists already")


@app.route("/profile/<profile_id>", methods=["DELETE"])
def delete_one(profile_id):
    profile = Profile.query.filter(Profile.profile_id == profile_id).one_or_none()

    if profile is not None:
        db.session.delete(profile)
        db.session.commit()
        return "Profile successfuly deleted", 200
    else:
        abort(204, f"Profile with id {profile_id} cannot be deleted")


if __name__ == "__main__":
    app.run(debug=True)
