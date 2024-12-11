<?php
include('conn.php');

$query = 'select count(*) as total from usuario';
$resultado = mysqli_query($con, $query);
$fetch = mysqli_fetch_assoc($resultado);
$count = $fetch['total'];