-----------------------------------------------------------------------------------------

/*
.read lcer.sql
*/
.header on
.mode column
.nullvalue NULL

-- en mode développement/débugage, destruction de la table avant sa re-création
-- (une erreur surviendra si la table n'existe pas) :
drop table Produit;
drop table Client;
drop table Achat;

create table Produit(
    idp int primary key,
    nom varchar(20) not null,
    prix real not null,
    stock int not null,
    check(0<prix and prix<2000), -- valeurs possibles dans fourchette raisonnable 
    check(0<=stock and stock<10000) -- valeurs possibles dans fourchette raisonnable 
);

insert into Produit values(99,'peluche',5,1000);
insert into Produit values(95,'chemisier',20,500);
insert into Produit values(92,'cravate',15,9900);
insert into Produit values(97,'porsche',1000,12);

create table Client(
    idc int primary key,
    nom varchar(20) not null,
    age int,
    adresse varchar(20) not null,
    debit real not null,
    check(0<age and age<=130), -- valeurs possibles dans fourchette raisonnable 
    check(0<=debit and debit<2000) -- valeurs possibles dans fourchette raisonnable 
);

insert into Client values(27,'Rita',17,'Rio',20);
insert into Client values(29,'Riton',18,'Cayeux',0);
insert into Client values(23,'Jeanne',19,'New York',300);

create table Achat(
    ida int primary key,
    idp int not null,
    idc int not null, 
    expedie varchar(3) not null,
    foreign key (idp) references Produit(idp),
    foreign key (idc) references Client(idc),
    check(expedie='oui' or expedie='non')
);

insert into Achat values(1,99,29,'oui');
insert into Achat values(2,95,27,'non');
insert into Achat values(3,99,23,'non');
insert into Achat values(4,97,27,'oui');

select * from Produit;
select * from Client;
select * from Achat;


-----------------------------------------------------------------------------------------
