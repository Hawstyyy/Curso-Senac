CREATE DATABASE Mercadin;
USE Mercadin;

CREATE TABLE EX2_CLIENTE(
	codcliente int auto_increment,
    nome VARCHAR(100) NOT NULL,
    datanascimento VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) NOT NULL,
    PRIMARY KEY (codcliente)
);

CREATE TABLE EX2_PEDIDO(
	codpedido INT auto_increment,
    codcliente INT,
    datapedido VARCHAR(100) NOT NULL,
    nf VARCHAR(100) NOT NULL,
    valortotal FLOAT NOT NULL,
    FOREIGN KEY (codcliente) REFERENCES EX2_CLIENTE(codcliente),
    PRIMARY KEY (codpedido)
);

create table EX2_PRODUTO(
	codproduto INT auto_increment,
    descricao varchar(100) not null,
    quantidade int not null,
    primary key (codproduto)
    );

CREATE TABLE EX2_ITEMPEDIDO(
	codpedido INT auto_increment,
    numeroitem INT,
    valorunitario FLOAT not null,
    quantidade INT not null,
    codproduto INT,
    FOREIGN KEY (codpedido) REFERENCES EX2_PEDIDO(codpedido),
    FOREIGN KEY (codproduto) REFERENCES EX2_PRODUTO(codproduto),
    primary key (numeroitem)
);

create table EX2_LOG(
	codlog INT auto_increment,
    data varchar(50),
    descricao varchar(100),
    primary key (codlog)
);

create table EX2_REQUISICAO_COMPRA(
	codrequisicaocompra int auto_increment,
    codproduto int,
    data varchar(100) not null,
    quantidade int not null,
    primary key (codrequisicaocompra),
    foreign key (codproduto) references EX2_PRODUTO(codproduto)
);

insert into EX2_CLIENTE (nome, datanascimento, cpf) values ("Braiani", "1991-10-28", "123.123.123-12");
select * from EX2_ITEMPEDIDO;

insert into EX2_CLIENTE (nome, datanascimento, cpf) values ("Cliente 3", "1234-12-12", "123.123.123-12"), 
("Cliente 4", "1234-12-12", "123.123.123-12"), 
("Cliente 5", "1234-12-12", "123.123.123-12"), 
("Cliente 6", "1234-12-12", "123.123.123-12"), 
("Cliente 7", "1234-12-12", "123.123.123-12"), 
("Cliente 8", "1234-12-12", "123.123.123-12"), 
("Cliente 9", "1234-12-12", "123.123.123-12"), 
("Cliente 10", "1234-12-12", "123.123.123-12");

insert into EX2_PRODUTO (descricao, quantidade) values ("produto", "10"),
("produto", "10"), 
("produto", "10"), 
("produto", "10"), 
("produto", "10"), 
("produto", "10"), 
("produto", "10"), 
("produto", "10");

insert into EX2_PEDIDO (codcliente ,datapedido, nf, valortotal) values (1,"2024-12-12", "123", 1000.00),
(2,"2024-12-12", "123", 1000.00), 
(3,"2024-12-12", "123", 1000.00), 
(4,"2024-12-12", "123", 1000.00), 
(5,"2024-12-12", "123", 1000.00);

insert into EX2_ITEMPEDIDO (numeroitem, valorunitario, quantidade, codproduto) values (1, 10.00, 10, 1),
(2, 10.00, 10, 2), 
(3, 10.00, 10, 3), 
(4, 10.00, 10, 4), 
(5, 10.00, 10, 5);