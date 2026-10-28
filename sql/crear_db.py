import sqlite3

conn = sqlite3.connect('cafeteria.db')
cursor = conn.cursor()
with open("script.sql", "r", encoding = "utf-8") as archivo:
    script_sql = archivo.read()

cursor.executescript(script_sql)
conn.commit()
conn.close()

print("Listo, se creo y aprendi")