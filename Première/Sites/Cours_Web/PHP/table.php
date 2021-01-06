<?php
   if (isset($_GET["valeur"])){
      $valeur = $_GET["valeur"];
   }else{
      $valeur = 10;
   }
?>
<!DOCTYPE html>
<html lang = "fr">
   <head>
      <title>Table</title>
      <meta charset = "utf-8">
   </head>
   <body>
      <form action = "table.php">
         Valeur :
         <input type = "text" name = "valeur">
         <button type = "submit">Calculer</button>
      </form>
      <ul>
      <?php
         for ($i = 0; $i <= 10; $i = $i + 1){
            $style = "";
            if ($i % 2 != 0){
               $style = "background:gray; color:white";
            }
            echo "<li style = '" . $style . "'>";
            echo $valeur . " * " . $i . " = " . ($valeur * $i);
            echo "</li>\n";
         }
      ?>
      </ul>
   </body>
</html>

