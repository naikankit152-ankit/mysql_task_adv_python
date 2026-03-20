import mysql.connector


conn = mysql.connector.connect(
    user="root",
    password="ankitnaik18",
    host="localhost",
    port=3306,
    database="gietu"
)
if conn.is_connected():
  print("connected")

cur = conn.cursor()
cur.execute("SHOW DATABASES")
for x in cur:
  print(x)

cur.execute("SELECT * FROM giet")
for x in cur:
    print(x)

cur.execute("SELECT name FROM giet;")
for x in cur:
    print(x)

cur.execute("SELECT name, address FROM giet;")
for x in cur:
    print(x)

cur.execute("SELECT roll, salary FROM giet;")
for x in cur:
    print(x)

cur.execute("SELECT * FROM giet WHERE name = 'aman';")
for x in cur:
    print(x)


cur.execute("SELECT * FROM giet WHERE address = 'delhi';")
for x in cur:
    print(x)


cur.execute("SELECT * FROM giet WHERE gender = 'M';")
for x in cur:
    print(x)

cur.execute("SELECT * FROM giet WHERE desig = 'doctor';")
for x in cur:
    print(x)

cur.execute("SELECT * FROM giet WHERE salary = 15000;")
for x in cur:
    print(x)

cur.execute("SELECT * FROM giet WHERE salary > 20000;")
for x in cur:
    print(x)

cur.execute("SELECT * FROM giet WHERE salary < 30000;")
for x in cur:
    print(x)

cur.execute("SELECT * FROM giet WHERE gender='M' AND salary > 20000;")
for x in cur:
    print(x)

cur.execute("SELECT * FROM giet WHERE gender='F' OR address='raipur';")
for x in cur:
    print(x)

cur.execute("SELECT * FROM giet WHERE name LIKE 'a%';")
for x in cur:
    print(x)

cur.execute("SELECT * FROM giet WHERE name LIKE '%h';")
for x in cur:
    print(x)

cur.execute("SELECT * FROM giet WHERE address LIKE '%pur%';")
for x in cur:
    print(x)

cur.execute("SELECT * FROM giet ORDER BY name ASC;")
for x in cur:
    print(x)

cur.execute("SELECT * FROM giet ORDER BY salary DESC;")
for x in cur:
    print(x)

cur.execute("SELECT COUNT(*) FROM giet;")
for x in cur:
    print(x)

cur.execute("SELECT COUNT(*) FROM giet WHERE gender='M';")
for x in cur:
    print(x)

conn.close()
cur.close()
conn.close()