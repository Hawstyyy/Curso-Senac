CREATE DATABASE Mercadin;
USE Mercadin;

CREATE TABLE CLIENTE(
	cod_cliente INT,
    nome VARCHAR(100) NOT NULL,
    data_nasc VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) NOT NULL,
    PRIMARY KEY (cod_cliente)
);

CREATE TABLE PEDIDO(
	cod_pedido INT,
    cod_cliente INT,
    datapedido VARCHAR(100) NOT NULL,
    nf VARCHAR(100) NOT NULL,
    valor_total FLOAT NOT NULL,
    FOREIGN KEY (cod_cliente) REFERENCES CLIENTE(cod_cliente),
    PRIMARY KEY (cod_pedido)
);

create table PRODUTO(
	cod_produto INT,
    descricao varchar(100) not null,
    quantidade int not null,
    primary key (cod_produto)
    );

CREATE TABLE ITEMPEDIDO(
	cod_pedido INT,
    numero_item INT not null,
    valor_unitario FLOAT not null,
    quantidade INT not null,
    cod_produto INT,
    FOREIGN KEY (cod_pedido) REFERENCES PEDIDO(cod_pedido),
    FOREIGN KEY (cod_produto) REFERENCES PRODUTO(cod_produto)
);

create table LOG(
	cod_log INT,
    data varchar(50),
    descricao varchar(100),
    primary key (cod_log)
);

create table REQUISICAO(
	cod_requisicao int,
    cod_produto int,
    data varchar(100) not null,
    quantidade int not null,
    primary key (cod_requisicao),
    foreign key (cod_produto) references PRODUTO(cod_produto)
);