## Importing SQL/Engine

from sqlalchemy import create_engine
import sqlite3

engine = create_engine('sqlite:///zillowdata.db', echo=True)

sqlite_connection = engine.connect()

## Reading in CSVs

west_la_df = pd.read_csv('west_la.csv')

central_la_df = pd.read_csv('central_la.csv')

east_la_df = pd.read_csv('east_la.csv')

south_la_df = pd.read_csv('south_la.csv')

the_valley_df = pd.read_csv('the_valley.csv')

san_gabriel_valley_df = pd.read_csv('san_gabriel_valley.csv')

census_df = pd.read_csv('censusdata.csv')

## West LA CSV to SQL Table

sqlite_table = 'westla'
west_la_df.to_sql(sqlite_table, sqlite_connection, if_exists='update')

## Central LA CSV to SQL Table

sqlite_table = 'centralla'
central_la_df.to_sql(sqlite_table, sqlite_connection, if_exists='update')

## South LA CSV to SQL Table

sqlite_table = 'southla'
south_la_df.to_sql(sqlite_table, sqlite_connection, if_exists='update')

## East LA CSV to SQL Table

sqlite_table = 'eastla'
east_la_df.to_sql(sqlite_table, sqlite_connection, if_exists='update')

## South Bay CSV to SQL Table

sqlite_table = 'southbay'
south_bay_df.to_sql(sqlite_table, sqlite_connection, if_exists='update')

## The Valley CSV to SQL Table

sqlite_table = 'thevalley'
the_valley_df.to_sql(sqlite_table, sqlite_connection, if_exists='update')

## San Gabriel Valley CSV to SQL Table

sqlite_table = 'sangabrielvalley'
san_gabriel_df.to_sql(sqlite_table, sqlite_connection, if_exists='update')

## Income Census Data CSV to SQL Table

sqlite_table = 'censusdata'
census_df.to_sql(sqlite_table, sqlite_connection, if_exists='update')

## Okay time to close up SQL!

sqlite_connection.close()