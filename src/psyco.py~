import psycopg2

conn = psycopg2.connect("dbname=ilf_json user=greg")
cur = conn.cursor()	

#script_file = open('schema.sql', 'r')
#cur.execute(script_file.read())
cur.execute('DROP TABLE IF EXISTS "UZYTKOWNIK" CASCADE;');

cur.execute('SELECT * FROM "SERIE";');
x = cur.fetchone()
print x
	
conn.close()

	


