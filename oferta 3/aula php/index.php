<?php

$nome = 'Enzo';
$sobrenome = 'Lopez';
$idade = 18;
$cidade = 'Campo grande';
$curso = 'Voucher Desenvolvedor';

echo "Hello world";
echo "<h1 style='color: green;'> Enzo </h1>";
// echo $nome;
echo $nome . ' ' . $sobrenome;

echo '<br>';
$quantia = strlen($nome);
$endereco = 'abababa';

echo "seu nome é $nome, ele tem $quantia caracteres <br>";
echo "Olá $nome, seu novo endereço: $endereco foi registrado no sistema";
echo "Meu nome é $nome, tenho $idade anos, moro na cidade de $cidade, e faço o curso de $curso";

echo '<br>';

$nota1 = 8.5;
$nota2 = 7;
$media = ($nota1 + $nota2) / 2;

echo "$media";

echo '<br>';

$valor = 100;
$desconto = 100 - (($valor * 10) / 100);

echo $desconto;
