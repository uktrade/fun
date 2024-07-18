import duckdb

# The code in this file defines test data schema and values. 
# You can see here the table structures defined by the DDL statements. 
# The `copy <tablename>` from statement is used to copy data from csv files to the tables. 
# The test data itself is stored in the `data` folder. 

duckdb.sql("""
create table Countries(
     Id     int primary key
    ,Name   varchar
);

copy Countries
from 'derec/data/Countries.csv'
(auto_detect true)
""")
           
duckdb.sql("""
create table GdpGrowthRates (
     Id         int primary key
    ,CountryId  int
    ,Value      int
    ,foreign key (CountryId) references Countries(Id)
);

copy GdpGrowthRates
from 'derec/data/GdpGrowthRates.csv'
(auto_detect true);
""")
           
duckdb.sql("""
create table WhiskeyTypes (
     Id         int primary key
    ,Type       varchar(32)
);

copy WhiskeyTypes 
from 'derec/data/WhiskeyTypes.csv'
(auto_detect true);
""")

duckdb.sql("""
create table WhiskeyExports (
     Id             int primary key
    ,CountryId      int
    ,WhiskeyType    int
    ,Value          int
    ,foreign key (CountryId) references Countries(Id)
    ,foreign key (WhiskeyType) references WhiskeyTypes(Id)
);

copy WhiskeyExports 
from 'derec/data/WhiskeyExports.csv'
(auto_detect true);
""")
