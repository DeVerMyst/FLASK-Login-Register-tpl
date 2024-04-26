Environnement viruel: `python -m venv .venv`
Windows: `.\.venv\Scripts\activate`
Macos: `source .venv/bin/activate`

**Interface (partie 1) pour gérer un login/register**

A partir d'un template (base.html)
* page d'accueil (index.html)
* login (login.html)
    * un champ login (nom et ou mail)
    * un champ mot de passe
    * bouton envoyer
* s'enregistrer (register.html)
    * un champ login (nom ou mail)
    * un champ mot de passe
    * un champ mot de passe
    * bouton envoyer

Faire une interface en flask avec un dossier:
* templates
    * les fichiers html
* models
    * model.py 
* routes
    * route.py
* modules
    * create_session.py

Utiliser bootstrap et sqlite. 

Quelques lignes de route, une fois le register ou le login validé on retourne sur la page d'accueil.

Utilisons tous la même classe user
```python 
Class User():
    id = ...
    username = ...
    password = ... 
```
