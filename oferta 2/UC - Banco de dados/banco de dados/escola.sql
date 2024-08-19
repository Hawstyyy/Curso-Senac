create database escola;
use escola;

create table alunos(
	matricula int auto_increment,
    nome varchar(30) not null,
    email varchar(50),
    primary key (matricula)
);

insert into alunos(matricula, nome, email) values (null, "Enzo", "email");
select * from alunos;

