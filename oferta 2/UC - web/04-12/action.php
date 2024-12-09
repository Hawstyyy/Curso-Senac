<?php
include('./conn.php');
session_start();

$nome = mysqli_real_escape_string($con, $_POST['nome']);
$senha = mysqli_real_escape_string($con, $_POST['password']);

if (empty($nome) || empty($senha)) {
  header('location: index.php');
  exit();
}

$query = "select * from usuario where nome = '{$nome}' and senha = '{$senha}'";
$resultado = mysqli_query($con, $query);
$row = mysqli_num_rows($resultado);
$retorno = mysqli_fetch_array($resultado);

if ($row) {
  $_SESSION['nome'] = $nome;
  $_SESSION['setor'] = $retorno['setor'];
  if ($_SESSION['setor'] == 'admin') {
    header('location: ./admin.php');
    exit();
  }
  else if ($_SESSION['setor'] == 'user') {
    header('location: ./user.php');
    exit();
  }
}

else {
  $_SESSION['erro'] = 'Erro, Verifique os campos e tente novamente';
  header('location: index.php');
  exit();
}