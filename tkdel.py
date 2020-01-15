import sqlite3
conn=sqlite3.connect("demo2.db")
with conn:
	cur=conn.cursor()
	cur.execute("DELETE from Doctor where id='4'")
	print("RECORD is Deleted")