create database sprint_5;
use sprint_5;

create table Curso(
  idCurso int auto-increment primary key,
  nome varchar(50),
  sigla varchar(3),
  coordenador varchar(50)
);


insert into Curso (nome, sigla, coordenador) values
('Engenharia de Computação', 'EC', 'Dr. Carlos Silva'),
('Matemática Aplicada', 'MA', 'Profa. Ana Costa'),
('Física Geral', 'FG', 'Dr. Pedro Almeida');

-- a) Exibir todos os dados da tabela.
select * from Curso;
-- b) Exibir apenas os coordenadores dos cursos.
select coordenador from Curso;
-- c) Exibir apenas os dados dos cursos de uma determinada sigla.
select * from Curso where sigla = 'EC';
-- d) Exibir os dados da tabela ordenados pelo nome do curso.
select * from Curso order by nome;
-- e) Exibir os dados da tabela ordenados pelo nome do coordenador em ordem
-- decrescente.
select * from Curso order by nome desc;
-- f) Exibir os dados da tabela, dos cursos cujo nome comece com uma determinada letra.
select * from Curso where nome like 'E%';
-- g) Exibir os dados da tabela, dos cursos cujo nome termine com uma determinada letra.
select * from Curso where nome like '%A';
-- h) Exibir os dados da tabela, dos cursos cujo nome tenha como segunda letra uma
-- determinada letra.
select * from Curso where nome like '_A%';
-- i) Exibir os dados da tabela, dos cursos cujo nome tenha como penúltima letra uma
-- determinada letra.
select * from Curso where nome like '%A_'
-- j) Elimine a tabela.
truncate Curso;