import sqlite3
import os
os.chdir(r'D:\sqlite_opros_6')
con=sqlite3.connect('books02.db')
createtable = '''
CREATE TABLE IF NOT EXISTS author  (
    id_author INTEGER PRIMARY KEY AUTOINCREMENT,
    author_name TEXT,
    author_descr TEXT
);
CREATE TABLE IF NOT EXISTS style  (
    id_style INTEGER PRIMARY KEY AUTOINCREMENT,
    style_name TEXT
);
CREATE TABLE IF NOT EXISTS book  (
    id_book INTEGER PRIMARY KEY AUTOINCREMENT,
    id_author INTEGER,
    id_style INTEGER,
    title TEXT,
    description TEXT,
    number_ex INTEGER
);
'''
cur = con.cursor() 
cur.executescript(createtable)

tuple01=[3,"Poema"]
sql_tuple01="INSERT INTO style VALUES (?,?)"
cur.execute(sql_tuple01,tuple01)
tuple02=("Rasskaz")
sql_tuple02="INSERT INTO style(style_name) VALUES (?)"
cur.execute(sql_tuple02,tuple02)

cur.close()
con.commit()
con.close()
