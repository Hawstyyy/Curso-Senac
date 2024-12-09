<?php
session_start();
if (empty($_SESSION['nome']) || !$_SESSION['nome']) {
  header('location: index.php');
  $_SESSION['erro'] = 'Por favor, logue primeiro';
}