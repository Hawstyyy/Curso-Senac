<?php
if (empty($_SESSION['nome']) || !$_SESSION['nome']) {
  header('location: index.php');
}