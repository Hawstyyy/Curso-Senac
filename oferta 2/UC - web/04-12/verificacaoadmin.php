<?php
if ($_SESSION['setor'] != 'admin'){
  $_SESSION['erro'] = 'Você não tem acesso a esse painel'
  header('location: usuario.php');
  exit();
}
?>