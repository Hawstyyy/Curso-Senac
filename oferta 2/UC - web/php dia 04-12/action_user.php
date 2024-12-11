<?php 
include('verificacao.php');
include('conn.php');

session_start();

$first_name = mysqli_real_escape_string($con, $_POST['first_name']);
$last_name = mysqli_real_escape_string($con, $_POST['last_name']);
$fone = mysqli_real_escape_string($con, $_POST['fone']);
$address = mysqli_real_escape_string($con, $_POST['address']);
$email = mysqli_real_escape_string($con, $_POST['email']);
$sexo = mysqli_real_escape_string($con, $_POST['sexo']);

if (empty($first_name) || empty($last_name) || empty($fone) || empty($address) || empty($email) || empty($sexo)) {
  $_SESSION['erro'] = 'por favor preencha todos os campos';
  header('location: ./user.php');
  exit();
}

else {
  $query = "insert into clientes values (null, '{$first_name}', '{$last_name}', '{$sexo}', '{$fone}', '{$address}', '{$email}')";
  $result = mysqli_query($con, $query);

  if ($result == '') {
    echo "<script language: javascript> window.alert('Não foi possível efetuar o cadastro');
    window.location.href='user.php';</script>";
    exit();
  }

  else {
    echo "<script language: javascript> window.alert('Cadastro efetuado com sucesso');
    window.location.href='user.php';</script>";
    exit();
  }
  exit();
}