drop database if exists banco;
create database banco;
use banco;
set sql_safe_updates = 0;

create table estado(
  id_estado int primary key auto_increment,
  estado varchar(100)
);

create table cidade(
  id_cidade int primary key auto_increment,
  id_estado int,
  cidade varchar(100),
  foreign key (id_estado) references estado(id_estado)
);

create table agencias(
  id_agencia int primary key auto_increment,
  numero_agencia varchar(100),
  endereco varchar(100),
  id_cidade int,
  id_estado int,
  foreign key (id_cidade) references cidade(id_cidade),
  foreign key (id_estado) references estado(id_estado)
);

create table genero(
  id_genero int primary key auto_increment,
  genero enum("Masculino", "Feminino", "Outro")
);

create table raca(
  id_raca int primary key auto_increment,
  raca enum("Branco", "Preto", "Amarelo", "Pardo", "Indigena")
);

create table religiao(
  id_religiao int primary key auto_increment,
  religiao varchar(100)
);

create table clientes(
  id_cliente int primary key auto_increment,
  nome varchar(100),
  cpf varchar(13),
  rg varchar(12),
  data_nascimento date,
  telefone varchar(18),
  endereco varchar(100),
  saldo float,
  numero_conta varchar(50),
  id_raca int,
  id_religiao int,
  id_cidade int,
  id_estado int,
  foreign key (id_cidade) references cidade(id_cidade),
  foreign key (id_estado) references estado(id_estado),
  foreign key (id_raca) references raca(id_raca),
  foreign key (id_religiao) references religiao(id_religiao)
);

create table saque(
  id_operacao int primary key auto_increment,
  id_agencia int,
  id_cliente int,
  saque float,
  foreign key (id_agencia) references agencias(id_agencia),
  foreign key (id_cliente) references clientes(id_cliente)
);

create table deposito(
  id_operacao int primary key auto_increment,
  id_agencia int,
  id_cliente int,
  deposito float,
  foreign key (id_agencia) references agencias(id_agencia),
  foreign key (id_cliente) references clientes(id_cliente)
);

INSERT INTO estado (estado) VALUES ('São Paulo'), ('Rio de Janeiro'), ('Minas Gerais'), ('Bahia');

INSERT INTO cidade (id_estado, cidade) VALUES 
(1, 'São Paulo'), 
(1, 'Campinas'), 
(2, 'Rio de Janeiro'), 
(3, 'Belo Horizonte'), 
(4, 'Salvador');

INSERT INTO agencias (numero_agencia, endereco, id_cidade, id_estado) VALUES 
('0001', 'Avenida Paulista, 100', 1, 1), 
('0002', 'Rua da Praia, 200', 2, 2), 
('0003', 'Praça da Liberdade, 300', 3, 3), 
('0004', 'Rua da Bahia, 400', 4, 4);

INSERT INTO genero (genero) VALUES ('Masculino'), ('Feminino'), ('Outro');

INSERT INTO raca (raca) VALUES ('Branco'), ('Preto'), ('Amarelo'), ('Pardo'), ('Indigena');

INSERT INTO religiao (religiao) VALUES ('Cristianismo'), ('Islamismo'), ('Ateísmo'), ('Espiritismo');

INSERT INTO clientes (nome, cpf, rg, data_nascimento, telefone, endereco, saldo, numero_conta, id_raca, id_religiao, id_cidade, id_estado) VALUES 
('João Silva', '12345678900', 'MG1234567', '1990-01-01', '(11) 91234-5678', 'Rua A, 1', 200.00, '12345-6', 1, 1, 1, 1),
('Maria Souza', '23456789001', 'MG2345678', '1985-05-05', '(21) 92345-6789', 'Rua B, 2', 2000.00, '23456-7', 2, 2, 2, 2);

delimiter $
create trigger saque_cliente
before insert on saque
for each row
begin
  declare saldo_atual float;
  select saldo into saldo_atual from clientes where id_cliente = new.id_cliente;
  
  if saldo_atual > 0 then
    update clientes set saldo = saldo - NEW.saque where id_cliente = NEW.id_cliente;
  else
    signal sqlstate '45000' set message_text = 'Saldo insuficiente';
  end if;

end$
delimiter ;

INSERT INTO saque (id_agencia, id_cliente, saque) VALUES 
(1, 1, 200.00), 
(2, 2, 300.00);

delimiter $
create trigger deposito_cliente
before insert on deposito
for each row
begin
  update clientes set saldo = saldo + NEW.deposito where id_cliente = NEW.id_cliente;
  
end$
delimiter ;

INSERT INTO deposito (id_agencia, id_cliente, deposito) VALUES 
(1, 1, 500.00), 
(3, 2, 700.00);
