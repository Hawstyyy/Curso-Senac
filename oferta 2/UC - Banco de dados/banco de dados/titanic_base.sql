create database if not exists titanic_base;
use titanic_base;

create table titanic_base(
  PassengerId int primary key,
  Survived int,
  Pclass int,
  Nome varchar(100),
  Sex varchar(20),
  Age varchar(20),
  SibSp int,
  Parch int,
  Ticket varchar(30),
  Fare float,
  Cabin varchar(20),
  Embarked varchar(10)
);

select * from titanic_base;
-- Quantas pessoas sobreviveram?
select count(*) from titanic_base where survived = 1;
-- Quantas crianças abaixo de 12 anos sobrevivera?
select count(*) from titanic_base where survived = 1 and age <= 12;