from flask import Flask
from modules.create_session import create_db
from routes.route import route_all


app = Flask(__name__)
app.secret_key = "ma_cle_secrete"

# Créez la session de base de données
session = create_db()
route_all(app, session)

# Exécutez l'application Flask
if __name__ == "__main__":
    app.run(debug=True, port=8080)
