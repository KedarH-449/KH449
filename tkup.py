import sqlite3
conn=sqlite3.connect("demo2.db")
with conn:
	cur=conn.cursor()
	cur.execute("UPDATE Doctor SET Name='Kedar'where id='4'")
	print("RECORD updated")