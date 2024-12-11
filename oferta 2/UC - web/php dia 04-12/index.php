  <!DOCTYPE html>
  <html lang="pt-br">
  <head>
    <meta charset="UTF-8">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <?php
    session_start();
    if (isset($_SESSION['erro'])) { ?>
      <span class='erro'><?php echo $_SESSION['erro']; unset($_SESSION['erro']);?></span>
    <?php } 
    ?>
    <form action="action.php" method="post" class="forms">
      <label for="nome">Nome:</label><br>
      <input type="text" id="nome" name="nome"><br>
      <label for="senha">Senha:</label><br>
      <input type="password" id="password" name="password"><br>
      <button type="submit">Entrar</button>
    </form>
  </body>
  </html>