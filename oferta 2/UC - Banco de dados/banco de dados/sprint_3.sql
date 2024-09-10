create table sprint_3;
use sprint_3;

create table Filme(
  idFilme int primary key auto_increment,
  titulo varchar(50),
  genero varchar(40),
  diretor varchar(40)
);

INSERT INTO Filme (titulo, genero, diretor) VALUES
('The Dark Knight', 'Ação', 'Christopher Nolan'),
('Inception', 'Ficção Científica', 'Christopher Nolan'),
('Pulp Fiction', 'Crime', 'Quentin Tarantino'),
('Kill Bill', 'Ação', 'Quentin Tarantino'),
('The Matrix', 'Ficção Científica', 'Lana Wachowski'),
('The Matrix Reloaded', 'Ficção Científica', 'Lana Wachowski'),
('The Shawshank Redemption', 'Drama', 'Frank Darabont');

-- • Exibir todos os dados da tabela.
select * from Filme;
-- • Adicionar o campo protagonista do tipo varchar(50) na tabela;
alter table Filme add column protagonista varchar(50);
-- • Atualizar o campo protagonista de todas os filmes inseridos;
update Filme set protagonista = 'Christian Bale' where idFilme = 1;
update Filme set protagonista = 'Leonardo DiCaprio' where idFilme = 2;
update Filme set protagonista = 'John Travolta' where idFilme = 3;
update Filme set protagonista = 'Uma Thurman' where idFilme = 4;
update Filme set protagonista = 'Keanu Reeves' where idFilme = 5;
update Filme set protagonista = 'Keanu Reeves' where idFilme = 6;
update Filme set protagonista = 'Tim Robbins' where idFilme = 7;

-- • Modificar o campo diretor do tamanho 40 para o tamanho 150;
ALTER TABLE Filme MODIFY diretor VARCHAR(150);
-- • Atualizar o diretor do filme com id=5;
update Filme set diretor = 'Jonathan Nolan' where idFilme = 5;
-- • Atualizar o diretor dos filmes com id=2 e com o id=7;
update Filme set diretor = 'Lilly Wachowski' where idFilme = 5 or idFilme = 7;
-- • Atualizar o título do filme com o id=6;
update Filme set titulo = 'The Matrix Revolutions' where idFilme = 6;
-- • Excluir o filme com o id=3;
delete from Filme where idFilme = 3;
-- • Exibir os filmes em que o gênero é diferente de drama;
select * from Filme where genero != 'Drama';
-- • Exibir os dados dos filmes que o gênero é igual ‘suspense’;
select * from Filme where genero == 'Suspense';
-- • Descrever os campos da tabela mostrando a atualização do campo protagonista e
-- diretor;
describe Filme;
-- • Limpar os dados da tabela;
truncate Filme;