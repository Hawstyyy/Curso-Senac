<?php
session_start();
include('./conn.php');

$nome = mysqli_real_escape_string($con, $_POST['nome']);
$senha = mysqli_real_escape_string($con, $_POST['password']);

if (empty($nome) || empty($senha)) {
  $_SESSION['erro'] = 'Erro, os campos estão vazios tente novamente';
  header('location: index.php');
  exit();
}

$query = "select * from usuario where nome = '{$nome}' and senha = '{$senha}'";
$selectcount = "select count(*) from usuario";
$resultado = mysqli_query($con, $query);
$rescount = mysqli_query($con, $selectcount);
$row = mysqli_num_rows($resultado);
$retorno = mysqli_fetch_array($resultado);
$retorno2 = mysqli_fetch_array($rescount);

if ($row) {
  $_SESSION['nome'] = $nome;
  $_SESSION['setor'] = $retorno['setor'];
  if ($_SESSION['setor'] == 'admin') {
    header('location: admin.php');
    exit();
  }
  else if ($_SESSION['setor'] == 'user') {
    header('location: usuario.php');
  }
}

else if (!$row) {
  $_SESSION['erro'] = 'Erro, Verifique os campos e tente novamente';
  header('location: index.php');
  exit();
}
// if (empty($nome) || empty($senha)) {
//   header('location: conn.php');
//   exit();
// }
