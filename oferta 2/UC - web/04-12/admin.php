<?php
  include('action.php');
  include('verificacaoadmin.php');
?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard de Admin</title>
    <link rel="stylesheet" href="admin.css">
</head>
<body>
    <div class="container">
        <!-- Barra Lateral -->
        <aside class="sidebar">
            <div class="sidebar-header">
                <h2>Admin</h2>
            </div>
            <nav>
                <ul>
                    <li><a href="#">Painel</a></li>
                    <li><a href="#">Usuários</a></li>
                    <li><a href="#">Configurações</a></li>
                    <li><a href="#">Relatórios</a></li>
                    <li><a href="./sair.php">Logout</a></li>
                </ul>
            </nav>
        </aside>

        <!-- Conteúdo Principal -->
        <main class="main-content">
            <header>
                <h1>Dashboard</h1>
            </header>

            <section class="stats">
                <div class="stat-card">
                    <h3>Usuários</h3>
                    <p><?php echo count()?></p>
                </div>
                <div class="stat-card">
                    <h3>Vendas</h3>
                    <p>1280</p>
                </div>
                <div class="stat-card">
                    <h3>Relatórios</h3>
                    <p>15</p>
                </div>
                <div class="stat-card">
                    <h3>Comentários</h3>
                    <p>57</p>
                </div>
            </section>

            <section class="overview">
                <h2>Visão Geral</h2>
                <p>Aqui você pode adicionar gráficos ou mais informações sobre o desempenho.</p>
            </section>
        </main>
    </div>
</body>
</html>
