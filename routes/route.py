from flask import render_template


def route_all(app, session):

    # Définissez les routes de l'application
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/register", methods=["GET", "POST"])
    def register():
        return render_template("register.html")

    @app.route("/login", methods=["GET", "POST"])
    def login():
        return render_template("login.html")
