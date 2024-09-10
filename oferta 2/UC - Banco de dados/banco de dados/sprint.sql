create database sprint;
use sprint;

create table atleta(
  idAtleta int primary key auto_increment,
  nome varchar(40),
  modalidade varchar(40),
  qtdMedalha int
);

insert into atleta(nome, modalidade, qtdMedalha) values
 ('João Silva', 'Natação', 7),
 ('Ana Costa', 'Natação', 5),
 ('Carlos Souza', 'Natação', 3),
 ('Maria Oliveira', 'Atletismo', 5),
 ('Rafael Mendes', 'Atletismo', 2),
 ('Lúcia Pereira', 'Judô', 4),
 ('Rodrigo Lima', 'Judô', 6),
 ('Ana Santos', 'Ginástica Artística', 4),
 ('Paula Rocha', 'Ginástica Artística', 3),
 ('Lucas Pereira', 'Vôlei de Praia', 2),
 ('Fernanda Silva', 'Vôlei de Praia', 1);

set sql_safe_updates = 0;

-- • Exibir todos os dados da tabela.
select * from atleta;
-- • Atualizar a quantidade de medalhas do atleta com id=1;
update atleta set qtdMedalha = 8 where idAtleta = 1;
-- • Atualizar a quantidade de medalhas do atleta com id=2 e com o id=3;
update atleta set qtdMedalha = 6 where idAtleta = 2 or idAtleta = 3;
-- • Atualizar o nome do atleta com o id=4;
update atleta set nome = 'Lucas Varinei' where idAtleta = 4;
-- • Adicionar o campo dtNasc na tabela, com a data de nascimento dos atletas, tipo date;
alter table atleta add column dtNasc date;
-- • Atualizar a data de nascimento de todos os atletas;
update atleta set dtNasc = '1990-01-05' where idAtleta = 1;
update atleta set dtNasc = '1990-02-18' where idAtleta = 1;
update atleta set dtNasc = '1990-03-22' where idAtleta = 1;
update atleta set dtNasc = '1990-04-15' where idAtleta = 1;
update atleta set dtNasc = '1990-05-30' where idAtleta = 1;
update atleta set dtNasc = '1990-06-12' where idAtleta = 1;
update atleta set dtNasc = '1990-07-25' where idAtleta = 1;
update atleta set dtNasc = '1990-08-09' where idAtleta = 1;
update atleta set dtNasc = '1990-09-16' where idAtleta = 1;
update atleta set dtNasc = '1990-10-03' where idAtleta = 1;
update atleta set dtNasc = '1990-11-21' where idAtleta = 1;
-- • Excluir o atleta com o id=5;
delete from atleta where idAtleta = 5;
-- • Exibir os atletas onde a modalidade é diferente de natação;
select * from atleta where modalidade != 'Natação';
-- • Exibir os dados dos atletas que tem a quantidade de medalhas maior ou igual a 3;
select * from atleta where qtdMedalha >= 3;
-- • Modificar o campo modalidade do tamanho 40 para o tamanho 60;
alter table atleta modify modalidade varchar(60);
-- • Descrever os campos da tabela mostrando a atualização do campo modalidade;
describe atleta;
-- • Limpar os dados da tabela;
truncate atleta;