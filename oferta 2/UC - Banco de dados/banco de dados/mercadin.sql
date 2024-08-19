CREATE DATABASE Mercadin;
USE Mercadin;

CREATE TABLE EX2_CLIENTE(
	codcliente INT,
    nome VARCHAR(100) NOT NULL,
    datanascimento VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) NOT NULL,
    PRIMARY KEY (codcliente)
);

CREATE TABLE EX2_PEDIDO(
	codpedido INT,
    codcliente INT,
    datapedido VARCHAR(100) NOT NULL,
    nf VARCHAR(100) NOT NULL,
    valortotal FLOAT NOT NULL,
    FOREIGN KEY (codcliente) REFERENCES EX2_CLIENTE(codcliente),
    PRIMARY KEY (codpedido)
);

create table EX2_PRODUTO(
	codproduto INT,
    descricao varchar(100) not null,
    quantidade int not null,
    primary key (codproduto)
    );

CREATE TABLE EX2_ITEMPEDIDO(
	codpedido INT,
    numeroitem INT,
    valorunitario FLOAT not null,
    quantidade INT not null,
    codproduto INT,
    FOREIGN KEY (codpedido) REFERENCES EX2_PEDIDO(codpedido),
    FOREIGN KEY (codproduto) REFERENCES EX2_PRODUTO(codproduto),
    primary key (numeroitem)
);

create table EX2_LOG(
	codlog INT,
    data varchar(50),
    descricao varchar(100),
    primary key (codlog)
);

create table EX2_REQUISICAO_COMPRA(
	codrequisicaocompra int,
    codproduto int,
    data varchar(100) not null,
    quantidade int not null,
    primary key (codrequisicaocompra),
    foreign key (codproduto) references EX2_PRODUTO(codproduto)
);