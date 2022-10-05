from flask import render_template


def configure_routes(app):
    @app.route("/", methods=["GET", "POST"])
    def index():
        return render_template("index.html")
