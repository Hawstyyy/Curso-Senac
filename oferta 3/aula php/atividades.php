<?php
if (isset($_POST['num1'])) {
  $num1 = $_POST['num1'];
  $num2 = $_POST['num2'];

  $soma = $num1 + $num2;
  $subtracao = $num1 - $num2;
  $divisao = $num1 / $num2;
  $multi = $num1 * $num2;

  echo "$soma - soma - " . '' . gettype($soma) . '' . '<br>';
  echo "$subtracao - subtracao - " . '' . gettype($subtracao) . '' . '<br>';
  echo "$divisao - divisao - " . '' . gettype($divisao) . '' . '<br>';
  echo "$multi - multi - " . '' . gettype($multi) . '' . '<br>';
}

if (isset($_POST['idade'])) {
  $idade = $_POST['idade'];

  if ($idade < 18) {
    echo "menor de idade <br>";
  } else if ($idade >= 18 & $idade < 60) {
    echo "maior de idade <br>";
  } else if ($idade >= 60) {
    echo "maior de idade, pessoa idosa <br>";
  }
}


if (isset($_POST['atividade']) and $_POST['atividade'] == 3) {
  for ($i = 0; $i <= 100; $i++) {
    if ($i % 3 == 0 & $i % 5 == 0) {
      echo "AB <br>";
    } else if ($i % 3 == 0) {
      echo "A <br>";
    } else if ($i % 5 == 0) {
      echo "B <br>";
    } else {
      echo $i . '' . '<br>';
    }
  }
}

if (isset($_POST['largura'])) {
  function calcular_area($largura, $comprimento)
  {
    $area = $largura * $comprimento;
    echo $area;
  }

  $largura = $_POST['largura'];
  $comprimento = $_POST['comprimento'];

  calcular_area($largura, $comprimento);
}
if (isset($_POST['atividade']) & $_POST['atividade'] == 5) {
  $array = [];
  $array[] = 0;
  $array[] = 1;

  for ($count = 1; $count <= 10; $count++) {
    array_push($array, $array[$count] + $array[$count - 1]);
  }

  foreach ($array as $key => $value) {
    echo $value . '' . '<br>';
  }
}

if (isset($_POST['palavra'])) {
  function check($palavra)
  {
    $vogais = ['a', 'e', 'i', 'o', 'u'];
    for ($i = 0; $i < strlen($palavra); $i++) {
      foreach ($vogais as $vogal) {
        // echo $palavra[$i] == $vogal;
        if ($palavra[$i] == $vogal) {
          break;
        } else {
          echo $palavra[$i];
          break;
        }
      }
    }
  }
  $palavra = $_POST['palavra'];
  check($palavra);
}

if (isset($_POST['atividade']) & $_POST['atividade'] == 7) {
  echo date('D');
  echo ", " . ' ' . date('M');
  echo ' de' . ' ' . date('Y');
}

if (isset($_POST['atividade']) & $_POST['atividade'] == 8) {
  file_put_contents('notas.txt', file_get_contents('notas.txt') . '' . "- Final do conteúdo");
  echo file_get_contents('notas.txt');
}

if (isset($_POST['email'])) {
  $email = $_POST['email'];
  $count_arroba = 0;
  $count_ponto = 0;

  for ($i = 0; $i < strlen($email); $i++) {
    if ($email[$i] == '@') {
      $count_arroba++;
    } else if ($email[$i] == '.') {
      $count_ponto++;
    }
  }

  if ($count_arroba > 0 & $count_ponto > 0) {
    echo 'Email válido';
  } else {
    echo 'Email inválido';
  }
}

if (isset($_POST['idade_10']) & isset($_POST['nome'])) {
  $nome = $_POST['nome'];
  $idade = $_POST['idade_10'];
  echo "Olá, $nome! Você tem $idade anos!";
}
