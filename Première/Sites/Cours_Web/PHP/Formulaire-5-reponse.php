<!DOCTYPE html>
<html lang = "fr">
   <head>
      <title>Réponse au formulaire</title>
      <meta charset = "utf-8">
   </head>
   <body>
      <?php if ($_GET[ 'ident']=="admin" AND $_GET[ 'pass']=="admin" ) 
         { ?>
	      <h1>Bienvenue</h1>
	      <p>Voici la page administrateur du site</p>
      <?php 
         } else 
         {
         	echo '<p>Identifiant et/ou mot de passe incorrect</p>'; 
         } ?>
   </body>
</html>
