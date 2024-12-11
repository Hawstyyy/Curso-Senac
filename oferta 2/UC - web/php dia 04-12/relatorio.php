<?php
include('conn.php');
// include('verificacao.php');

$query = "SELECT * FROM produtos";
$resultado = mysqli_query($con, $query);
?>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product List</title>
    <style>
      /* Reset de estilos e layout básico */
      * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }

      body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f4;
        display: flex;
        min-height: 100vh;
      }

      h1 {
        text-align: center;
        margin-top: 20px;
        color: #333;
      }

      /* Estilos para a Sidebar */
      .sidebar {
        height: 100vh;
        width: 250px;
        background-color: #333;
        position: fixed;
        top: 0;
        left: 0;
        padding-top: 20px;
        box-shadow: 2px 0px 5px rgba(0, 0, 0, 0.1);
      }

      .sidebar ul {
        list-style-type: none;
        padding: 0;
      }

      .sidebar ul li {
        padding: 15px;
        text-align: center;
      }

      .sidebar ul li a {
        color: white;
        text-decoration: none;
        display: block;
      }

      .sidebar ul li a:hover {
        background-color: #575757;
      }

      /* Estilos para o conteúdo da página */
      .content {
        margin-left: 250px;
        padding: 20px;
        width: 100%;
      }

      /* Estilos da tabela */
      table {
        width: 100%;
        margin: 20px auto;
        border-collapse: collapse;
        background-color: #fff;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
      }

      th, td {
        padding: 12px;
        text-align: left;
        border-bottom: 1px solid #ddd;
      }

      th {
        background-color: #4CAF50;
        color: white;
      }

      tr:nth-child(even) {
        background-color: #f2f2f2;
      }

      tr:hover {
        background-color: #ddd;
      }

      td {
        color: #333;
      }

    </style>
  </head>
  <body>

    <!-- Sidebar -->
    <?php include('./sidebar.php'); ?>

    <!-- Conteúdo da página -->
    <div class="content">
      <h1>Product List</h1>
      <table>
        <thead>
          <tr>
            <th>Id</th>
            <th>Nome</th>
            <th>Descrição</th>
            <th>Valor</th>
          </tr>
        </thead>
        <tbody>
          <?php while ($retorno = mysqli_fetch_array($resultado)) { ?>
            <tr>
              <td><?php echo $retorno['id']; ?></td>
              <td><?php echo $retorno['nome']; ?></td>
              <td><?php echo $retorno['descricao']; ?></td>
              <td><?php echo $retorno['preco']; ?></td>
            </tr>
          <?php } ?>
        </tbody>
      </table>
    </div>
  </body>
</html>
