create database sprint;
use sprint;

create table Professor(
  idProfessor int primary key auto_increment,
  nome varchar(50),
  especialidade varchar(40),
  dtNasc date
);

INSERT INTO Professor (nome, especialidade, dtNasc) VALUES
('Ana Silva', 'Matemática', '1980-05-15'),
('Carlos Pereira', 'Física', '1975-09-23'),
('Mariana Souza', 'Química', '1982-11-30'),
('João Oliveira', 'Biologia', '1978-02-14'),
('Fernanda Costa', 'História', '1985-07-22'),
('Lucas Almeida', 'Geografia', '1983-03-10');

set sql_safe_updates = 0;

-- a) Exibir todos os dados da tabela.
select * from Professor;
-- b) Adicionar o campo funcao do tipo varchar(50), onde a função só pode ser ‘monitor’,
-- ‘assistente’ ou ‘titular’;
alter table Professor add column funcao varchar(50) enum('monitor', 'assistente', 'titular');
-- c) Atualizar os professores inseridos e suas respectivas funções;
update Professor set funcao = 'monitor' where idProfessor = 1;
update Professor set funcao = 'assistente' where idProfessor = 2;
update Professor set funcao = 'titular' where idProfessor = 3;
update Professor set funcao = 'monitor' where idProfessor = 4;
update Professor set funcao = 'assistente' where idProfessor = 5;
update Professor set funcao = 'titular' where idProfessor = 6;
-- d) Inserir um novo professor;
insert into Professor (nome, especialidade, dtNasc, funcao) values
('Ederson Costa', 'Matemática', '1990-03-30', 'monitor');
-- e) Excluir o professor onde o idProfessor é igual a 5;
delete from Professor where idProfessor = 5;
-- f) Exibir apenas os nomes dos professores titulares;
select * from Professor where funcao = 'titular';
-- g) Exibir apenas as especialidades e as datas de nascimento dos professores monitores;
select especialidade, dtNasc where funcao = 'monitores';
-- h) Atualizar a data de nascimento do idProfessor igual a 3;
update Professores set dtNasc = '1990-03-30' where idProfessor = 3;
-- i) Limpar a tabela Professor;
truncate Professor;