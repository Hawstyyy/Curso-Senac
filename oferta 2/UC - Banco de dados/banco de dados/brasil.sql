drop database brasil;
create database brasil;
use brasil;

create table estado_civil(
	id_estado_civil int auto_increment primary key,
    estado_civil varchar(100) not null
);

create table escolaridade(
  id_escolaridade int auto_increment primary key,
  escolaridade varchar(100) not null
);

create table raca(
  id_raca int auto_increment primary key,
  raca varchar(100) not null
);

create table nacionalidade(
  id_nacionalidade int auto_increment primary key,
  nacionalidade varchar(100) not null
);

create table sexo(
  id_sexo int auto_increment primary key,
  sexo varchar(100) not null
);

create table estado(
  id_estado int auto_increment primary key,
  estado varchar(100) not null
);

create table cidade(
  id_cidade int auto_increment primary key,
  cidade varchar(100) not null,
  id_estado int not null,
  foreign key cidade(id_estado) references estado(id_estado)
);
    
create table cadastro_de_cliente(
  CPF varchar(100) primary key,
  nome varchar(100) not null,
  RG varchar(100),
  id_cidade int not null,
  id_sexo int not null,
  id_nacionalidade int not null,
  fone varchar(100) not null,
  id_raca int not null,
  id_escolaridade int not null,
  id_estado_civil int not null,
  foreign key fk_estado_civil(id_estado_civil) references estado_civil(id_estado_civil),
  foreign key fk_cidade(id_cidade) references cidade(id_cidade),
  foreign key fk_sexo(id_sexo) references sexo(id_sexo),
  foreign key fk_nacionalidade(id_nacionalidade) references nacionalidade(id_nacionalidade),
  foreign key fk_raca(id_raca) references raca(id_raca),
  foreign key fk_escolaridade(id_escolaridade) references escolaridade(id_escolaridade)
); 

INSERT INTO estado (id_estado, estado) VALUES (null, "Acre"),
(null, "Alagoas"),
(null, "Amapá"),
(null, "Amazonas"),
(null, "Bahia"),
(null, "Ceará"),
(null, "Espírito Santo"),
(null, "Goiás"),
(null, "Maranhão"),
(null, "Mato Grosso"),
(null, "Mato Grosso do Sul"),
(null, "Minas Gerais"),
(null, "Pará"),
(null, "Paraíba"),
(null, "Paraná"),
(null, "Pernambuco"),
(null, "Piauí"),
(null, "Rio de Janeiro"),
(null, "Rio Grande do Norte"),
(null, "Rio Grande do Sul"),
(null, "Rondônia"),
(null, "Roraima"),
(null, "Santa Catarina"),
(null, "São Paulo"),
(null, "Sergipe"),
(null, "Tocantins");

INSERT INTO cidade(cidade, id_estado) VALUES("Rio Branco", 1);
INSERT INTO cidade(cidade, id_estado) VALUES("Cruzeiro do Sul", 1);
INSERT INTO cidade(cidade, id_estado) VALUES("Sena Madureira", 1);
INSERT INTO cidade(cidade, id_estado) VALUES("Tarauacá", 1);
INSERT INTO cidade(cidade, id_estado) VALUES("Feijó", 1);

INSERT INTO cidade(cidade, id_estado) VALUES("Maceió", 2);
INSERT INTO cidade(cidade, id_estado) VALUES("Arapiraca", 2);
INSERT INTO cidade(cidade, id_estado) VALUES("Palmeira dos Índios", 2);
INSERT INTO cidade(cidade, id_estado) VALUES("União dos Palmares", 2);
INSERT INTO cidade(cidade, id_estado) VALUES("Santana do Ipanema", 2);

INSERT INTO cidade(cidade, id_estado) VALUES("Macapá", 3);
INSERT INTO cidade(cidade, id_estado) VALUES("Santana", 3);
INSERT INTO cidade(cidade, id_estado) VALUES("Laranjal do Jari", 3);
INSERT INTO cidade(cidade, id_estado) VALUES("Oiapoque", 3);
INSERT INTO cidade(cidade, id_estado) VALUES("Mazagão", 3);

INSERT INTO cidade(cidade, id_estado) VALUES("Manaus", 4);
INSERT INTO cidade(cidade, id_estado) VALUES("Parintins", 4);
INSERT INTO cidade(cidade, id_estado) VALUES("Itacoatiara", 4);
INSERT INTO cidade(cidade, id_estado) VALUES("Coari", 4);
INSERT INTO cidade(cidade, id_estado) VALUES("Tefé", 4);

INSERT INTO cidade(cidade, id_estado) VALUES("Salvador", 5);
INSERT INTO cidade(cidade, id_estado) VALUES("Feira de Santana", 5);
INSERT INTO cidade(cidade, id_estado) VALUES("Vitória da Conquista", 5);
INSERT INTO cidade(cidade, id_estado) VALUES("Camaçari", 5);
INSERT INTO cidade(cidade, id_estado) VALUES("Ilhéus", 5);

INSERT INTO cidade(cidade, id_estado) VALUES("Fortaleza", 6);
INSERT INTO cidade(cidade, id_estado) VALUES("Caucaia", 6);
INSERT INTO cidade(cidade, id_estado) VALUES("Juazeiro do Norte", 6);
INSERT INTO cidade(cidade, id_estado) VALUES("Sobral", 6);
INSERT INTO cidade(cidade, id_estado) VALUES("Crato", 6);

INSERT INTO cidade(cidade, id_estado) VALUES("Vitória", 7);
INSERT INTO cidade(cidade, id_estado) VALUES("Vila Velha", 7);
INSERT INTO cidade(cidade, id_estado) VALUES("Cariacica", 7);
INSERT INTO cidade(cidade, id_estado) VALUES("Serra", 7);
INSERT INTO cidade(cidade, id_estado) VALUES("Guarapari", 7);

INSERT INTO cidade(cidade, id_estado) VALUES("Goiânia", 8);
INSERT INTO cidade(cidade, id_estado) VALUES("Anápolis", 8);
INSERT INTO cidade(cidade, id_estado) VALUES("Aparecida de Goiânia", 8);
INSERT INTO cidade(cidade, id_estado) VALUES("Rio Verde", 8);
INSERT INTO cidade(cidade, id_estado) VALUES("Luziânia", 8);

INSERT INTO cidade(cidade, id_estado) VALUES("São Luís", 9);
INSERT INTO cidade(cidade, id_estado) VALUES("Imperatriz", 9);
INSERT INTO cidade(cidade, id_estado) VALUES("Caxias", 9);
INSERT INTO cidade(cidade, id_estado) VALUES("Timon", 9);
INSERT INTO cidade(cidade, id_estado) VALUES("Bacabal", 9);

INSERT INTO cidade(cidade, id_estado) VALUES("Cuiabá", 10);
INSERT INTO cidade(cidade, id_estado) VALUES("Várzea Grande", 10);
INSERT INTO cidade(cidade, id_estado) VALUES("Rondonópolis", 10);
INSERT INTO cidade(cidade, id_estado) VALUES("Sinop", 10);
INSERT INTO cidade(cidade, id_estado) VALUES("Lucas do Rio Verde", 10);

INSERT INTO cidade(cidade, id_estado) VALUES("Campo Grande", 11);
INSERT INTO cidade(cidade, id_estado) VALUES("Dourados", 11);
INSERT INTO cidade(cidade, id_estado) VALUES("Três Lagoas", 11);
INSERT INTO cidade(cidade, id_estado) VALUES("Corumbá", 11);
INSERT INTO cidade(cidade, id_estado) VALUES("Ponta Porã", 11);

INSERT INTO cidade(cidade, id_estado) VALUES("Belo Horizonte", 12);
INSERT INTO cidade(cidade, id_estado) VALUES("Uberlândia", 12);
INSERT INTO cidade(cidade, id_estado) VALUES("Contagem", 12);
INSERT INTO cidade(cidade, id_estado) VALUES("Juiz de Fora", 12);
INSERT INTO cidade(cidade, id_estado) VALUES("Montes Claros", 12);

INSERT INTO cidade(cidade, id_estado) VALUES("Belém", 13);
INSERT INTO cidade(cidade, id_estado) VALUES("Ananindeua", 13);
INSERT INTO cidade(cidade, id_estado) VALUES("Santarém", 13);
INSERT INTO cidade(cidade, id_estado) VALUES("Marabá", 13);
INSERT INTO cidade(cidade, id_estado) VALUES("Parauapebas", 13);

INSERT INTO cidade(cidade, id_estado) VALUES("João Pessoa", 14);
INSERT INTO cidade(cidade, id_estado) VALUES("Campina Grande", 14);
INSERT INTO cidade(cidade, id_estado) VALUES("Santa Rita", 14);
INSERT INTO cidade(cidade, id_estado) VALUES("Patos", 14);
INSERT INTO cidade(cidade, id_estado) VALUES("Bayeux", 14);

INSERT INTO cidade(cidade, id_estado) VALUES("Curitiba", 15);
INSERT INTO cidade(cidade, id_estado) VALUES("Londrina", 15);
INSERT INTO cidade(cidade, id_estado) VALUES("Maringá", 15);
INSERT INTO cidade(cidade, id_estado) VALUES("Foz do Iguaçu", 15);
INSERT INTO cidade(cidade, id_estado) VALUES("Ponta Grossa", 15);

INSERT INTO cidade(cidade, id_estado) VALUES("Recife", 16);
INSERT INTO cidade(cidade, id_estado) VALUES("Olinda", 16);
INSERT INTO cidade(cidade, id_estado) VALUES("Jaboatão dos Guararapes", 16);
INSERT INTO cidade(cidade, id_estado) VALUES("Caruaru", 16);
INSERT INTO cidade(cidade, id_estado) VALUES("Petrolina", 16);

INSERT INTO cidade(cidade, id_estado) VALUES("Teresina", 17);
INSERT INTO cidade(cidade, id_estado) VALUES("Parnaíba", 17);
INSERT INTO cidade(cidade, id_estado) VALUES("Picos", 17);
INSERT INTO cidade(cidade, id_estado) VALUES("Floriano", 17);
INSERT INTO cidade(cidade, id_estado) VALUES("São Raimundo Nonato", 17);

INSERT INTO cidade(cidade, id_estado) VALUES("Rio de Janeiro", 18);
INSERT INTO cidade(cidade, id_estado) VALUES("Niterói", 18);
INSERT INTO cidade(cidade, id_estado) VALUES("Duque de Caxias", 18);
INSERT INTO cidade(cidade, id_estado) VALUES("São Gonçalo", 18);
INSERT INTO cidade(cidade, id_estado) VALUES("Nova Iguaçu", 18);

INSERT INTO cidade(cidade, id_estado) VALUES("Natal", 19);
INSERT INTO cidade(cidade, id_estado) VALUES("Mossoró", 19);
INSERT INTO cidade(cidade, id_estado) VALUES("Parnamirim", 19);
INSERT INTO cidade(cidade, id_estado) VALUES("Caicó", 19);
INSERT INTO cidade(cidade, id_estado) VALUES("Santa Cruz", 19);

INSERT INTO cidade(cidade, id_estado) VALUES("Porto Alegre", 20);
INSERT INTO cidade(cidade, id_estado) VALUES("Caxias do Sul", 20);
INSERT INTO cidade(cidade, id_estado) VALUES("Pelotas", 20);
INSERT INTO cidade(cidade, id_estado) VALUES("Santa Maria", 20);
INSERT INTO cidade(cidade, id_estado) VALUES("Gravataí", 20);

INSERT INTO cidade(cidade, id_estado) VALUES("Porto Velho", 21);
INSERT INTO cidade(cidade, id_estado) VALUES("Ji-Paraná", 21);
INSERT INTO cidade(cidade, id_estado) VALUES("Ariquemes", 21);
INSERT INTO cidade(cidade, id_estado) VALUES("Vilhena", 21);
INSERT INTO cidade(cidade, id_estado) VALUES("Guajará-Mirim", 21);

INSERT INTO cidade(cidade, id_estado) VALUES("Boa Vista", 22);
INSERT INTO cidade(cidade, id_estado) VALUES("Rorainópolis", 22);
INSERT INTO cidade(cidade, id_estado) VALUES("Caracaraí", 22);
INSERT INTO cidade(cidade, id_estado) VALUES("Mucajaí", 22);
INSERT INTO cidade(cidade, id_estado) VALUES("Pacaraima", 22);

INSERT INTO cidade(cidade, id_estado) VALUES("Florianópolis", 23);
INSERT INTO cidade(cidade, id_estado) VALUES("Joinville", 23);
INSERT INTO cidade(cidade, id_estado) VALUES("Blumenau", 23);
INSERT INTO cidade(cidade, id_estado) VALUES("São José", 23);
INSERT INTO cidade(cidade, id_estado) VALUES("Criciúma", 23);

INSERT INTO cidade(cidade, id_estado) VALUES("São Paulo", 24);
INSERT INTO cidade(cidade, id_estado) VALUES("Campinas", 24);
INSERT INTO cidade(cidade, id_estado) VALUES("São Bernardo do Campo", 24);
INSERT INTO cidade(cidade, id_estado) VALUES("Santo André", 24);
INSERT INTO cidade(cidade, id_estado) VALUES("Osasco", 24);

INSERT INTO cidade(cidade, id_estado) VALUES("Aracaju", 25);
INSERT INTO cidade(cidade, id_estado) VALUES("Nossa Senhora do Socorro", 25);
INSERT INTO cidade(cidade, id_estado) VALUES("Itabaiana", 25);
INSERT INTO cidade(cidade, id_estado) VALUES("Lagarto", 25);
INSERT INTO cidade(cidade, id_estado) VALUES("Estância", 25);

INSERT INTO cidade(cidade, id_estado) VALUES("Palmas", 26);
INSERT INTO cidade(cidade, id_estado) VALUES("Araguaína", 26);
INSERT INTO cidade(cidade, id_estado) VALUES("Paraíso do Tocantins", 26);
INSERT INTO cidade(cidade, id_estado) VALUES("Colinas do Tocantins", 26);
INSERT INTO cidade(cidade, id_estado) VALUES("Guaraí", 26);

insert into sexo(sexo) values("Masculino"),
("Feminino"),
("Outro");

insert into estado_civil(estado_civil) values ("Solteiro"),
("Casado"),
("Viúvo");

insert into nacionalidade(nacionalidade) values ("Brasileira"),
("Estrangeira");

insert into raca(raca) values ("Preto"),
("Pardo"),
("Branco"),
("Amarelo"),
("Indígena");

INSERT INTO escolaridade(escolaridade) VALUES("Ensino Fundamental Incompleto"),
("Ensino Fundamental Completo"),
("Ensino Médio Incompleto"),
("Ensino Médio Completo"),
("Curso Técnico"),
("Superior Incompleto"),
("Superior Completo"),
("Pós-Graduação");

INSERT INTO cadastro_de_cliente(CPF, nome, RG, id_cidade, id_sexo, id_nacionalidade, fone, id_raca, id_escolaridade, id_estado_civil) VALUES
("123.456.789-00", "Ana Silva", "MG-12.345.678", 1, 2, 1, "(11) 98765-4321", 2, 2, 1),
("234.567.890-01", "Carlos Souza", "SP-23.456.789", 2, 1, 1, "(21) 91234-5678", 1, 4, 2),
("345.678.901-12", "Maria Oliveira", "RJ-34.567.890", 3, 2, 1, "(31) 92345-6789", 3, 6, 3),
("456.789.012-23", "João Santos", "BA-45.678.901", 4, 1, 1, "(41) 93456-7890", 1, 5, 1),
("567.890.123-34", "Fernanda Costa", "PR-56.789.012", 5, 2, 1, "(51) 94567-8901", 2, 3, 2),
("678.901.234-45", "Roberto Lima", "CE-67.890.123", 6, 1, 1, "(61) 95678-9012", 4, 7, 3),
("789.012.345-56", "Lucia Almeida", "RS-78.901.234", 7, 2, 1, "(71) 96789-0123", 3, 8, 1),
("890.123.456-67", "Pedro Pereira", "MG-89.012.345", 8, 1, 1, "(81) 97890-1234", 5, 2, 2),
("901.234.567-78", "Juliana Martins", "SP-90.123.456", 9, 2, 1, "(91) 98901-2345", 2, 4, 3),
("012.345.678-90", "Felipe Ferreira", "RJ-01.234.567", 10, 1, 1, "(11) 99123-4567", 1, 6, 1),
("123.456.789-01", "Larissa Rocha", "BA-12.345.678", 11, 2, 1, "(21) 99234-5678", 3, 5, 2),
("234.567.890-12", "André Oliveira", "PR-23.456.789", 12, 1, 1, "(31) 99345-6789", 4, 8, 3),
("345.678.901-23", "Tatiane Souza", "SP-34.567.890", 13, 2, 1, "(41) 99456-7890", 1, 2, 1),
("456.789.012-34", "Gustavo Lima", "CE-45.678.901", 14, 1, 1, "(51) 99567-8901", 2, 3, 2),
("567.890.123-45", "Renata Carvalho", "RJ-56.789.012", 15, 2, 1, "(61) 99678-9012", 3, 7, 3),
("678.901.234-56", "Marcelo Rodrigues", "BA-67.890.123", 16, 1, 1, "(71) 99789-0123", 4, 4, 1),
("789.012.345-67", "Sofia Martins", "PR-78.901.234", 17, 2, 1, "(81) 99890-1234", 5, 6, 2),
("890.123.456-78", "Ricardo Mendes", "SP-89.012.345", 18, 1, 1, "(91) 99901-2345", 1, 5, 3),
("901.234.567-89", "Camila Pereira", "RJ-90.123.456", 19, 2, 1, "(11) 98876-5432", 2, 7, 1),
("012.345.678-01", "Diego Costa", "BA-01.234.567", 20, 1, 1, "(21) 98765-4321", 3, 8, 2),
("123.456.789-12", "Juliana Costa", "PR-12.345.678", 21, 2, 1, "(31) 97654-3210", 4, 4, 3),
("234.567.890-23", "Eduardo Santos", "SP-23.456.789", 22, 1, 1, "(41) 96543-2109", 5, 6, 1);

select nome, cidade from cadastro_de_cliente join cidade on cadastro_de_cliente.id_cidade = cidade.id_cidade;
select nome, estado from cadastro_de_cliente join estado on cadastro_de_cliente.id_cidade = estado.id_estado;
select nome, cpf, raca from cadastro_de_cliente join raca on cadastro_de_cliente.id_raca = raca.id_raca;
select nome, nacionalidade from cadastro_de_cliente join nacionalidade on cadastro_de_cliente.id_nacionalidade = nacionalidade.id_nacionalidade;
select nome, escolaridade from cadastro_de_cliente join escolaridade on cadastro_de_cliente.id_escolaridade = escolaridade.id_escolaridade;

select nome, cidade, estado, fone, rg, sexo, nacionalidade, raca, escolaridade from cadastro_de_cliente
join cidade on cadastro_de_cliente.id_cidade = cidade.id_cidade
join sexo on cadastro_de_cliente.id_sexo = sexo.id_sexo
join estado on cadastro_de_cliente.id_cidade = estado.id_estado
join raca on cadastro_de_cliente.id_raca = raca.id_raca
join nacionalidade on cadastro_de_cliente.id_nacionalidade = nacionalidade.id_nacionalidade
join escolaridade on cadastro_de_cliente.id_escolaridade = escolaridade.id_escolaridade;

-- atividade dia 04/09
SET SQL_SAFE_UPDATES = 0;
-- Se a letra da cidade começar de A até M, Mudar o nome da cidade para “Abaixo de M”, e de M até o final do alfabeto mudar o nome para “Acima de M”;
update cidade set cidade="Abaixo de M" where cidade < "M";
update cidade set cidade="Acima de M" where cidade > "M";

-- Os estados, deixaremos de utilizar seu nome, e sim sua região, então verifique a região do estado e altere, ex.: se o estado for Mato Grosso do Sul, você irá alterar o nome para “Centro Oeste”;
update estado set estado="Centro-Oeste" where estado="Mato Grosso do Sul" or estado ="Mato Grosso" or estado = "Goiás";
update estado set estado="Norte" where estado="Amapá" or estado="Amazonas" or estado ="Pará" or estado="Rondônia" or estado="Roraima" or estado="Tocantins" or estado="Acre";
update estado set estado="Nordeste" where estado="Alagoas" or estado="Bahia" or estado ="Ceará" or estado="Maranhão" or estado="Paraíba" or estado="Pernambuco" or estado="Piauí" or estado="Rio Grande do Norte" or estado="Sergipe";
update estado set estado="Sudeste" where estado="Espírito Santo" or estado="Minas Gerais" or estado="Rio de Janeiro" or estado="São Paulo";
update estado set estado="Sul" where estado="Paraná" or estado="Rio Grande do Sul" or estado="Santa Catarina";

-- Na nacionalidade, alterar estrangeiro para “Fora do Brasil”;
update nacionalidade set nacionalidade="Fora do Brasil" where nacionalidade="Estrangeira";

-- Nas raças, alterar para “seres humanos”;
update raca set raca="Seres humanos" where raca="Indígena" or raca="Preto" or raca="Pardo" or raca="Branco" or raca="Amarelo";

-- Na escolaridade mudaremos o padrão, tudo que for ensino fundamental ou médio, será alterado para “ensino básico”, e o que for de graduação para cima, será alterado para “ensino avançado”.
update escolaridade set escolaridade="Ensino básico" where escolaridade="Ensino Fundamental Completo" or escolaridade="Ensino Fundamental Incompleto" or escolaridade ="Ensino Médio Incompleto" or escolaridade="Ensino Médio Completo";
update escolaridade set escolaridade="Ensino avançado" where escolaridade="Superior Incompleto" or escolaridade="Superior Completo" or escolaridade="Pós-Graduação";
