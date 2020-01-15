import sqlite3
conn=sqlite3.connect("demo2.db")
with conn:
	cur = conn.cursor()
	cur.execute("SELECT * FROM Doctor")
	for row in cur.fetchall():
		print("id"+str(row[0]))
		print("Name"+row[1])
		print("Qualif"+row[2])
		print("Speci"+row[3])