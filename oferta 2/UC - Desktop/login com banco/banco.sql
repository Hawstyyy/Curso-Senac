create database CadastrosEdni;
use CadastrosEdni;
set SQL_SAFE_UPDATES = 0;

create table users(
  id int primary key auto_increment,
  nome varchar(255) not null,
  senha varchar(255) not null,
  texto varchar(255)
);

insert into users(nome, senha) values ('admin', 'admin');