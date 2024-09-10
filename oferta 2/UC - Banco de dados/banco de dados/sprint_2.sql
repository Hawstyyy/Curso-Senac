create database sprint;
use sprint;

create table Musica(
  idMusica int primary key auto_increment,
  titulo varchar(40),
  artista varchar(40),
  genero varchar(40)
);

insert into Musica(titulo, artista, genero) values
('Shape of You', 'Ed Sheeran', 'Pop'),
('Perfect', 'Ed Sheeran', 'Pop'),
('Blinding Lights', 'The Weeknd', 'Pop'),
('Save Your Tears', 'The Weeknd', 'Pop'),
('Smells Like Teen Spirit', 'Nirvana', 'Rock'),
('Come As You Are', 'Nirvana', 'Rock'),
('Take Five', 'Dave Brubeck', 'Jazz');

set sql_safe_updates = 0;

-- a) Exibir todos os dados da tabela.
select * from Musica;
-- b) Adicionar o campo curtidas do tipo int na tabela;
alter table Musica add column curtidas int;
-- c) Atualizar o campo curtidas de todas as músicas inseridas;
update Musica set curtidas = 40000 where idMusica = 1;
update Musica set curtidas = 40000 where idMusica = 2;
update Musica set curtidas = 40000 where idMusica = 3;
update Musica set curtidas = 40000 where idMusica = 4;
update Musica set curtidas = 40000 where idMusica = 5;
update Musica set curtidas = 40000 where idMusica = 6;
update Musica set curtidas = 40000 where idMusica = 7;
-- d) Modificar o campo artista do tamanho 40 para o tamanho 80;
alter table atleta modify artista varchar(80);
-- e) Atualizar a quantidade de curtidas da música com id=1;
update Musica set curtidas = 100000 where idMusica = 1;
-- f) Atualizar a quantidade de curtidas das músicas com id=2 e com o id=3;
update Musica set curtidas = 200000 where idMusica = 2 or idMusica = 3;
-- g) Atualizar o nome da música com o id=5;
update Musica set nome = 'Something in the Way' where idMusica = 5;
-- h) Excluir a música com o id=4;
delete from Musica where idAtleta = 4;
-- i) Exibir as músicas onde o gênero é diferente de funk;
select * from musica where genero != 'Funk'
-- j) Exibir os dados das músicas que tem curtidas maior ou igual a 20;
select * from musica where curtidas >= 20;
-- k) Descrever os campos da tabela mostrando a atualização do campo artista;
describe Musica;
-- l) Limpar os dados da tabela;
truncate Musica;