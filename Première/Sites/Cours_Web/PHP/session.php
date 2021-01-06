<?php
   session_start();
   if (!isset($_SESSION["compteur"])){
      $_SESSION["compteur"] = 0;
   }
   $_SESSION["compteur"] = $_SESSION["compteur"] + 1;
?>
<!DOCTYPE html>
<html lang = "fr">
   <head>
      <title>Chargement de la page</title>
      <meta charset = "utf-8">
   </head>
   <body>
      Page rechargée <?php echo $_SESSION["compteur"]; ?> fois.
   </body>
</html>
