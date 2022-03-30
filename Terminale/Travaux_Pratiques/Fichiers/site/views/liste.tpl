<!doctype html>
<html lang = "fr-FR">
    <head>
        <meta charset = "utf-8">
    </head>
    <body>

        % titres = ["id", "Prénom", "Nom", "Date de naissance", "Adresse", "Ville", "Code postal", "E-mail"]

        <table border = 1>
            <thead>
        % for titre in titres:
                <td>{{titre}}</td>
        % end
            </thead>
        % for ligne in lignes:
            <tr>
            % for col in ligne:
                <td>{{col}}</td>
            % end
            </tr>
        % end
        </table>

        <h2><a href = "/entreNouveau">Retourner à la page d'enregistrement</a></h2>
        <h2><a href = "/">Retourner à la page d'accueil</a></h2>
    </body>
</html>
