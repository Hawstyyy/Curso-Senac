CREATE DATABASE netflix;
USE netflix;

CREATE TABLE enderecos(
  id INT auto_increment,
  endereco VARCHAR(100),
);

CREATE TABLE catalogo(
  filme_id INT NOT NULL,
  serie_id INT NOT NULL,
  documentarios_id INT NOT NULL,
  FOREIGN KEY (filme_id) REFERENCES filmes(id),
  FOREIGN KEY (serie_id) REFERENCES serie(id),
  FOREIGN KEY (documentarios_id) REFERENCES documentarios(id),
)

CREATE TABLE filmes(
  id INT auto_increment,
  titulo VARCHAR(200) NOT NULL,
  ano_prod INT NOT NULL,
  duration VARCHAR(200) NOT NULL
);

CREATE TABLE episodios(
  id INT auto_increment,
  titulo VARCHAR(200) NOT NULL,
  ano_prod INT NOT NULL,
  duration VARCHAR(200) NOT NULL,
  temporada INT NOT NULL,
  prox_episodio INT NOT NULL,
  avaliacao INT,
);

CREATE TABLE series(
  id INT auto_increment,
  titulo VARCHAR(200) NOT NULL,
  ano_prod INT NOT NULL,
  duration VARCHAR(200) NOT NULL,
  temporada INT NOT NULL,
  episodio INT NOT NULL,
  FOREIGN KEY (episodio) REFERENCES episodios(id)
);

CREATE TABLE produtoras(
  id INT auto_increment,
  nome_prod VARCHAR(100) NOT NULL
);

CREATE TABLE documentarios(
  id INT auto_increment,
  titulo VARCHAR(200) NOT NULL,
  ano_prod INT NOT NULL,
  duration VARCHAR(200) NOT NULL,
  produtora INT NOT NULL,
  FOREIGN KEY (produtora) REFERENCES produtoras(id)
);

CREATE TABLE usuarios(
  id INT auto_increment,
  email VARCHAR(100) NOT NULL,
  senha VARCHAR(100) NOT NULL,
  telefone VARCHAR(100) NOT NULL,
  cpf VARCHAR(100) NOT NULL,
  endereco INT NOT NULL,
  cartao VARCHAR(100) NOT NULL,
  mensalidade FLOAT NOT NULL,
  FOREIGN KEY (endereco) REFERENCES enderecos(id)
);

CREATE TABLE cobranca(
  id INT auto_increment,
  dia INT NOT NULL,
  mes INT NOT NULL,
  mensalidade_pen INT NOT NULL
);