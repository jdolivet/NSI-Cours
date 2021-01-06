<!DOCTYPE html>
<html lang = "fr">
   <head>
      <title>Réponse au formulaire</title>
      <meta charset = "utf-8">
   </head>
   <body>
      <ul>
         <li>La valeur du nom est <b><?php echo $_POST['nom']?></b>
         </li>
         <li>La valeur du prénom est <b><?php echo  $_POST['prenom']?></b>
         </li>
         <li>La valeur de l'âge est <b><?php echo  $_POST['age']?></b>
         </li>
      </ul>
   </body>
</html>
