-----------------------------------------------------------------------------------------
-- tp_schema.sql


/*
.read tp_schema.sql
*/
.header on
.mode column
.nullvalue NULL

drop table bateau;
drop table marin;
drop table croisiere;
drop table equipage;

create table bateau(
    idb int primary key,
    nom varchar(20),
    capitaine varchar(20),
    port varchar(22),
    nbplaces int,
    style int,
    prix int
);

create table marin(
    idm int primary key,
    nom varchar(20),
    ville varchar(20),
    niveau int,
    avoir int
);

create table croisiere(
    idc int primary key,
    idb int, 
    jour date,
    foreign key (idb) references bateau(idb)
);

create table equipage(
    idc int, 
    idm int,
    foreign key (idc) references croisiere(idc),
    foreign key (idm) references marin(idm)
);

-- (les contraintes hors clés ne sont pas fournies dans ce fichier)

-----------------------------------------------------------------------------------------
