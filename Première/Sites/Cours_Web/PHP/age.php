<?php
   $annee = date("Y");
   $age = $annee - $_GET["a"];
?>
<!DOCTYPE html>
<html lang = "fr">
   <head>
      <title>Voici votre âge</title>
      <meta charset = "utf-8">
   </head>
   <body>
      Vous avez <?php echo $age; ?> ans cette année
   </body>
</html>
