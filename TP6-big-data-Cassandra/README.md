# BIG_DATA_TP6-Cassandra
```js
#تشغيل Cassandra داخل Docker
docker run -d --name mon-cassandra -p 9042:9042 cassandra:latest
# الدخول إلى cqlsh
docker exec -it mon-cassandra cqlsh
#نقل الملفات CSV إلى داخل الـ container 
docker cp restaurants.csv mon-cassandra:/
docker cp restaurants_inspections.csv mon-cassandra:/
#إنشاء الـ Keyspace والجداول داخل cqlsh
CREATE KEYSPACE IF NOT EXISTS resto_NY
WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor': 1 };

USE resto_NY;
#إنشاء جدول Restaurant
CREATE TABLE Restaurant (
    id INT,
    name VARCHAR,
    borough VARCHAR,
    buildingnum VARCHAR,
    street VARCHAR,
    zipcode INT,
    phone TEXT,
    cuisinetype VARCHAR,
    PRIMARY KEY (id)
);
CREATE INDEX fk_Restaurant_cuisine ON Restaurant (cuisinetype);
#إنشاء جدول Inspection
CREATE TABLE Inspection (
    idrestaurant INT,
    inspectiondate date,
    violationcode VARCHAR,
    violationdescription VARCHAR,
    criticalflag VARCHAR,
    score INT,
    grade VARCHAR,
    PRIMARY KEY (idrestaurant, inspectiondate)
);
CREATE INDEX fk_Inspection_Restaurant ON Inspection (grade);
#استيراد البيانات داخل cqlsh
COPY Restaurant (id, name, borough, buildingnum, street, zipcode, phone, cuisinetype)
FROM '/restaurants.csv' WITH DELIMITER=',';

COPY Inspection (idrestaurant, inspectiondate, violationcode, violationdescription, criticalflag, score, grade)
FROM '/restaurants_inspections.csv' WITH DELIMITER=',';
#السؤال 1 — Liste de tous les restaurants
cqlsh:resto_ny> SELECT * FROM Restaurant;

 id       | borough       | buildingnum | cuisinetype                                                      | name                                             | phone      | street                      | zipcode
----------+---------------+-------------+------------------------------------------------------------------+--------------------------------------------------+------------+-----------------------------+---------
 40786914 | STATEN ISLAND |        1465 |                                                         American |                                    BOSTON MARKET | 7188151198 |               FOREST AVENUE |   10302
 40366162 |        QUEENS |       11909 |                                                         American |                                 LENIHAN'S SALOON | 7188469770 |             ATLANTIC AVENUE |   11418
 41692194 |     MANHATTAN |         360 |                                                             Thai |                                    BANGKOK HOUSE | 2125415943 |            WEST   46 STREET |   10036
 41430956 |      BROOKLYN |        2225 |                                                        Caribbean |                                TJ'S TASTY CORNER | 7184844783 |               TILDEN AVENUE |   11226
...
 50017802 |    QUEENS |        9040     |                                                            Other |                                  HEALTHY HENRY'S | 3475007435 |                    160TH ST |   11432
 41288479 | MANHATTAN |        4001     |                                                 CafÃ©/Coffee/Tea |                                        STARBUCKS | 9175210342 |                    BROADWAY |   10032

(25624 rows)
# السؤال 2 — Liste des noms de restaurants
cqlsh:resto_ny> SELECT name FROM Restaurant;

 name
--------------------------------------------------
                                    BOSTON MARKET
                                 LENIHAN'S SALOON
                                    BANGKOK HOUSE
                                TJ'S TASTY CORNER
...
                                   HEALTHY HENRY'S
                                         STARBUCKS

(25624 rows)
#السؤال 3 — Nom et quartier du restaurant dont l’id = 41569764
cqlsh:resto_ny> SELECT name, borough
            ... FROM Restaurant
            ... WHERE id = 41569764;

 name    | borough
---------+----------
 BACCHUS | BROOKLYN

(1 rows)
#السؤال 4 — Dates et grades des inspections de ce restaurant
cqlsh:resto_ny> SELECT inspectiondate, grade
            ... FROM Inspection
            ... WHERE idrestaurant = 41569764;

 inspectiondate | grade
----------------+-------
     2013-06-27 |  null
     2013-07-08 |     A
     2013-12-26 |  null
     2014-02-05 |     A
     2014-07-17 |  null
     2014-08-06 |     A
     2015-01-08 |     A
     2016-02-25 |     A

(8 rows)

#السؤال 5 — Noms des restaurants de cuisine Française (French)
cqlsh:resto_ny> SELECT name
            ... FROM Restaurant
            ... WHERE cuisinetype = 'French';

 name
--------------------------------
                        MATISSE
                        ALMANAC
                   TOUT VA BIEN
                          FELIX
...
                      CAFE DADA
           BAR SUZETTE CREPERIE

(351 rows)
# السؤال 6 — Noms des restaurants situés dans BROOKLYN
cqlsh:resto_ny> CREATE INDEX resto_borough_idx ON Restaurant (borough);
cqlsh:resto_ny> SELECT name
            ... FROM Restaurant
            ... WHERE borough = 'BROOKLYN';

 name
--------------------------------------------
                          TJ'S TASTY CORNER
                             KING'S KITCHEN
                         LEO'S DELI & GRILL
                           JIN SUSHI & THAI
...
                                   RED ROSE
                 TSOB-TSOBE CAFE LOUNGE BAR

(6260 rows)
#السؤال 7 — Grades et scores pour le restaurant 41569764 avec score ≥ 10
cqlsh:resto_ny> SELECT grade, score
            ... FROM Inspection
            ... WHERE idrestaurant = 41569764
            ... AND score >= 10
            ... ALLOW FILTERING;

 grade | score
-------+-------
  null |    19
     A |    10

(2 rows)
#السؤال 8 — Grades (non nulls) des inspections dont score > 30
cqlsh:resto_ny> SELECT grade
            ... FROM Inspection
            ... WHERE score > 30 AND grade > ''
            ... ALLOW FILTERING;

 grade
----------------
              C
              C
              C
 Not Yet Graded
...
              Z
              C

(1152 rows)

Warnings :
Read 7436 live rows and 5203 tombstone cells for query SELECT grade, score FROM resto_ny.inspection WHERE token(idrestaurant) >= token(50018028) AND grade > '' AND score > 30 LIMIT 100 ALLOW FILTERING; token 9222309874911565378 (see tombstone_warn_threshold)

#السؤال 9 — Nombre de lignes retournées par la requête précédente
cqlsh:resto_ny> SELECT count(*)
            ... FROM Inspection
            ... WHERE score > 30 AND grade > ''
            ... ALLOW FILTERING;

 count
-------
  1152

(1 rows)

Warnings :
Aggregation query used without partition key

Read 14602 live rows and 10199 tombstone cells for query SELECT grade, score FROM resto_ny.inspection WHERE grade > '' AND score > 30 LIMIT 100 ALLOW FILTERING; token -7442997124414533764 (see tombstone_warn_threshold)
...
```js




