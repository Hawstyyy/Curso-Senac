create database sprint_6;
use sprint_6;

create table Revista(
  idRevista int auto-increment primary key,
  nome varchar(40),
  categoria varchar(30)
);

INSERT INTO Revista (nome) VALUES
('National Geographic'),
('Scientific American'),
('Time'),
('Forbes');

-- • Exibir todos os dados da tabela.
select * from Revista;
-- • Atualize os dados das categorias das 3 revistas inseridas. Exibir os dados da tabela
-- novamente para verificar se atualizou corretamente.
update Revista set categoria = 'Ciência, natureza, história, viagens e aventura' where idRevista = 1;
update Revista set categoria = 'Ciência e tecnologia' where idRevista = 2;
update Revista set categoria = 'Notícias, política, negócios, saúde e cultura ' where idRevista = 3;
update Revista set categoria = 'Negócios, finanças, tecnologia e empreendedorismo' where idRevista = 4;
-- • Insira mais 3 registros completos.
create database sprint_6;
use sprint_6;

create table Revista(
  idRevista int auto-increment primary key,
  nome varchar(40),
  categoria varchar(30)
);

INSERT INTO Revista (nome) VALUES
('National Geographic'),
('Scientific American'),
('Time'),
('Forbes');

-- • Exibir todos os dados da tabela.
select * from Revista;
-- • Atualize os dados das categorias das 3 revistas inseridas. Exibir os dados da tabela
-- novamente para verificar se atualizou corretamente.
update Revista set categoria = 'Ciência, natureza, história, viagens e aventura' where idRevista = 1;
update Revista set categoria = 'Ciência e tecnologia' where idRevista = 2;
update Revista set categoria = 'Notícias, política, negócios, saúde e cultura ' where idRevista = 3;
update Revista set categoria = 'Negócios, finanças, tecnologia e empreendedorismo' where idRevista = 4;
-- • Insira mais 3 registros completos.
create database sprint_6;
use sprint_6;

create table Revista(
  idRevista int auto-increment primary key,
  nome varchar(40),
  categoria varchar(30)
);

INSERT INTO Revista (nome) VALUES
('National Geographic'),
('Scientific American'),
('Time'),
('Forbes');

-- • Exibir todos os dados da tabela.
select * from Revista;
-- • Atualize os dados das categorias das 3 revistas inseridas. Exibir os dados da tabela
-- novamente para verificar se atualizou corretamente.
update Revista set categoria = 'Ciência, natureza, história, viagens e aventura' where idRevista = 1;
update Revista set categoria = 'Ciência e tecnologia' where idRevista = 2;
update Revista set categoria = 'Notícias, política, negócios, saúde e cultura ' where idRevista = 3;
update Revista set categoria = 'Negócios, finanças, tecnologia e empreendedorismo' where idRevista = 4;
select * from Revista;
-- • Insira mais 3 registros completos.
INSERT INTO Revista (nome, categoria) VALUES
('Nature', 'Ciência e pesquisa acadêmica'),
('The Economist', 'Economia, política, negócios, ciência e tecnologia'),
('Wired', 'Tecnologia, cultura e negócios');
-- • Exibir novamente os dados da tabela.
select * from Revista;
-- • Exibir a descrição da estrutura da tabela.
describe Revista;
-- • Alterar a tabela para que a coluna categoria possa ter no máximo 40 caracteres.
alter table Revista modify categoria varchar (40);
-- • Exibir novamente a descrição da estrutura da tabela, para verificar se alterou o
-- tamanho da coluna categoria
SELECT * FROM Revista;
-- • Acrescentar a coluna periodicidade à tabela, que é varchar(15).
alter table Revista add column periodicidade varchar(15);
-- • Exibir os dados da tabela.
select * from Revista;
-- • Excluir a coluna periodicidade da tabela.
ALTER TABLE Revista DROP COLUMN periodicidade;