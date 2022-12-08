-----------------------------------------------------------------------------------------
-- tp_insertions.sql
-- Ce fichier contient des lignes pour les tables créées dans le script tp_schema.sql.

/*
.read tp_insertions.sql
*/
.header on
.mode column
.nullvalue NULL

delete from bateau;
delete from marin;
delete from croisiere;
delete from equipage;

-- colonnes : idb, nom, capitaine, port, nbplaces, style, prix
insert into bateau values(1,'La Licorne','François de Hadoque','Moulinsart',100,1,10);
insert into bateau values(2,'Toccata','Christian','Saint-Valery-sur-Somme',3,1,5);
insert into bateau values(3,'Foggy Dew','Isabelle','Le Havre',2,1,5);
insert into bateau values(4,'L''Hermione','La Fayette','Rochefort',50,0,10);
insert into bateau values(5,'La Santa Maria','Christophe Colomb','Palos',20,1,10);

-- colonnes : idm, nom, ville, niveau, avoir
insert into marin values(10,'Tintin','Bruxelles',1,20);
insert into marin values(11,'Haddock','Moulinsart',1,20);
insert into marin values(12,'Tournesol','Bruxelles',0,20);
insert into marin values(13,'Castafiore','Milan',0,20);
insert into marin values(14,'Dupond','Bruxelles',0,20);
insert into marin values(15,'Dupont','Bruxelles',0,20);
insert into marin values(16,'Rita','Vincennes',1,20);
insert into marin values(17,'Riton','Paname',1,20);
insert into marin values(18,'Jeanne','Rio',0,20);
insert into marin values(19,'Jules','Roanne',0,20);
insert into marin values(20,'Jim','New York',0,20);

-- colonnes : idc, idb, jour
insert into croisiere values(100,1,'01/07/2023');
insert into croisiere values(101,2,'15/09/2024');
insert into croisiere values(102,2,'31/12/2028');
insert into croisiere values(103,2,'01/01/2033');
insert into croisiere values(104,3,'15/09/2025');
insert into croisiere values(105,4,'15/09/2029');

-- colonnes :  idc, idm 
insert into equipage values(105,18);
insert into equipage values(105,19);
insert into equipage values(105,20);

insert into equipage values(100,10);
insert into equipage values(100,11);
insert into equipage values(100,16);
insert into equipage values(100,17);

insert into equipage values(101,16);
insert into equipage values(101,17);

insert into equipage values(102,10);
insert into equipage values(102,11);

insert into equipage values(104,16);
insert into equipage values(104,17);

insert into equipage values(105,12);
insert into equipage values(105,13);
insert into equipage values(105,14);
insert into equipage values(105,15);
insert into equipage values(105,10);

select * from bateau;
select * from marin;
select * from croisiere;
select * from equipage;

-----------------------------------------------------------------------------------------
