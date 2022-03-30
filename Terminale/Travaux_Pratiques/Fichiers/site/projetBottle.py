from bottle import route, post, template, request, run
import sqlite3


# La racine du site
@route('/')
def index():
    return template("index.tpl")
 
 # le formulaire d'inscription
@route("/entreNouveau")
def entreNouveau():
    return template("eleve.tpl")

# inscription des données du formulaire dans la BDD
@post("/ajouteEntree")
def ajouteEntree():
    connexion = sqlite3.connect("baseEleve.db")
    prenom = request.forms.getunicode("prenom") 
    # A compléter
    connexion.execute(...) # A compléter
    connexion.commit()
    connexion.close()
    return template("index.tpl")

# liste des eleves
@route("/liste")
def liste():
    connexion = sqlite3.connect("baseEleve.db")
    curseur = connexion.execute("SELECT * FROM eleve")
    lines = curseur.fetchall()
    connexion.close()
    return template("liste.tpl", lignes=lines)

# moteur de recherche
@route("/recherche")
def recherche():
    return template("recherche.tpl")
z
# resultats du moteur de recherche
@post("/requete")
def requete():
    # A compléter
    
# centres d'examens 
@route("/centreExamens")
def centres():
    # A compléter


# Procédure pour créer la base de données à la première utilisation
def creation():
    # A compléter
    
creation()
# on ouvre un serveur en local sur le port 7000 par exemple
run(reloader = True, debug = True, host='127.0.0.1', port=7000)