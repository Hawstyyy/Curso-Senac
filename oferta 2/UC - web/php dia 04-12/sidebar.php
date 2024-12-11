<!-- sidebar.php -->
<style>
  /* styles.css */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  display: flex;
  min-height: 100vh;
}

/* Sidebar */
.sidebar {
  height: 100vh;
  width: 250px;
  background-color: #333;
  position: fixed;
  top: 0;
  left: 0;
  padding-top: 20px;
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
  color: #fff;
}

/* Conteúdo da página */
.content {
  margin-left: 250px;
  padding: 20px;
  flex: 1;
}


</style>
<div class="sidebar">
  <ul>
    <li><a href="relatorio.php">Relatorio</a></li>
    <li><a href="user.php">Cadastro usuario</a></li>
    <li><a href="sair.php">Sair</a></li>
    <!-- Adicione mais links conforme necessário -->
  </ul>
</div>
