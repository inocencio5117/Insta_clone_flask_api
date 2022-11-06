from flask import render_template, jsonify, request
from config import app


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/health_check")
def health_check():
    return "This route is healthy "


@app.route("/colors/<palette>/")
def colors(palette):
    """Example endpoint returning a list of colors by palette
    This is using docstrings for specifications.
    ---
    parameters:
      - name: palette
        in: path
        type: string
        enum: ['all', 'rgb', 'cmyk']
        required: true
        default: all
    definitions:
      Palette:
        type: object
        properties:
          palette_name:
            type: array
            items:
              $ref: '#/definitions/Color'
      Color:
        type: string
    responses:
      200:
        description: A list of colors (may be filtered by palette)
        schema:
          $ref: '#/definitions/Palette'
        examples:
          rgb: ['red', 'green', 'blue']
    """
    all_colors = {
        "cmyk": ["cyan", "magenta", "yellow", "black"],
        "rgb": ["red", "green", "blue"],
    }
    if palette == "all":
        result = all_colors
    else:
        result = {palette: all_colors.get(palette)}

    return jsonify(result)


@app.route("/profile", methods=["GET", "POST"])
def create_profile():
    if request.method == "POST":
        data = request.data
        return data
    if request.method == "GET":
        return None


if __name__ == "__main__":
    app.run(debug=True)
