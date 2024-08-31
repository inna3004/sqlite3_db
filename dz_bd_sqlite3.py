import  sqlite3 as sl

con = sl.connect('thecode.db')

with con:
    con.execute("""
    CREATE TABLE account(
    user_id serial PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(355) UNIQUE NOT NULL,
    created_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP
    );
    CREATE TABLE table name (
   column_name TYPE column_constraint,
   table_constraint table_constraint
     ) INHERITS exiting_table_name;
    """)