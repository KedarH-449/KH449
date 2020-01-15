import sqlite3
conn=sqlite3.connect("demo2.db")
with conn:
	cur=conn.cursor()
	cur.execute("INSERT INTO Doctor(Name,Qualif,Speci)values('kishor','MBBS','CSE')")
	print("RECORD inserted")