from flask import render_template, request, redirect, url_for, flash
from models.model import User
from werkzeug.security import generate_password_hash, check_password_hash


def route_all(app, session):

    # Définissez les routes de l'application
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/register", methods=["GET", "POST"])
    def register():
        # POST
        if request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]
            confirm_password = request.form["confirm_password"]

            print("=" * 20)
            print(username, password, confirm_password)

            if password != confirm_password:
                flash("Les mots de passe sont différents", "error")
                return redirect(url_for("register"))

            if len(password) < 3:
                flash("Le mot de passe est trop short!!!", "error")
                return redirect(url_for("register"))

            # vérifier si l'utilisateur existe
            existing_user = session.query(User).filter_by(username=username).first()
            if existing_user:
                flash("L'utilisateur existe", "error")
                return redirect(url_for("register"))

            hashed_password = generate_password_hash(password)
            new_user = User(username=username, password=hashed_password)
            session.add(new_user)
            session.commit()
            flash("BRAVO", "success")
            return redirect(url_for("register"))

        return render_template("register.html")

    @app.route("/login", methods=["GET", "POST"])
    def login():
        # POST
        if request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]
            # vérifier si l'utilisateur existe
            existing_user = session.query(User).filter_by(username=username).first()
            if not existing_user:
                flash("L'utilisateur n'existe pas", "error")
                return redirect(url_for("register"))

            condition = check_password_hash(existing_user.password, password)
            if condition:
                flash("Utilisateur connecté", "success")
                return redirect(url_for("index"))
            else:
                flash("Utilisateur inconnu", "error")
                return redirect(url_for("login"))

        return render_template("login.html")
