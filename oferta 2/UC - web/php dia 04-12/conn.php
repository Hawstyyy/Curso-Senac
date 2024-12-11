<?php
$host = '10.28.2.16';
$usuario = 'suporte';
$senha = 'suporte';
$db = 'banco139';

$con = new mysqli($host, $usuario, $senha, $db);

if ($con -> connect_errno) {
  echo 'falha na conexão: ('. $con -> connect_errno. ")". con -> connect_error;
}