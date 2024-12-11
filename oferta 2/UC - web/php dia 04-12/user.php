<?php 
  include('verificacao.php');
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Perfil de Usuário</title>
  <link rel="stylesheet" href="user.css">
</head>
<body>
  <!-- Incluindo a Sidebar -->
  <?php include('sidebar.php'); ?>

  <div class="container">
    <?php
    if (isset($_SESSION['erro'])) { ?>
      <span class='erro'><?php echo $_SESSION['erro']; unset($_SESSION['erro']);?></span>
    <?php } 
    ?>
    
    <h1><?php echo "Bem-vindo, " . $_SESSION['nome']; ?></h1>
    <form action="action_user.php" method="post">
      Nome: <input type="text" name="first_name"><br>
      Sobrenome: <input type="text" name="last_name"><br>
      Fone: <input type="text" name="fone"><br>
      Endereço: <input type="text" name="address"><br>
      Email: <input type="text" name="email"><br>
      Sexo: <input type="text" name="sexo"><br>
      <button type="submit">Enviar</button>
    </form>
  </div>
</body>
</html>
