create database if not exists laptop_prices;
use laptop_prices;

create table laptop_prices(
  Company varchar(100),
  Product varchar(100),
  TypeName varchar(100),
  Inches float,
  Ram int,
  OS varchar(100),
  Weight float,
  Price_euros float,
  Screen varchar(100),
  ScreenW int,
  ScreenH int,
  Touchscreen varchar(100),
  IPSpanel varchar(100),
  RetinaDisplay varchar(100),
  CPU_company varchar(100),
  CPU_freq float,
  CPU_model varchar(100),
  PrimaryStorage int,
  SecondaryStorage int,
  PrimaryStorageType varchar(100),
  SecondaryStorageType varchar(100),
  GPU_company varchar(100),
  GPU_model varchar(100)
);

select count(*) from laptop_prices;
-- quantidade de notebooks com windows, MacOS e linux
select count(*) from laptop_prices where OS = 'Windows 10';
select count(*) from laptop_prices where OS = 'Macos';
select count(*) from laptop_prices where OS = 'Linux';
-- notebook de menor preço
select * from laptop_prices where Price_euros = (select min(Price_euros) from laptop_prices);
-- notebook de maior preço
select * from laptop_prices where Price_euros = (select max(Price_euros) from laptop_prices);
-- media de preços
select avg(price_euros) from laptop_prices;