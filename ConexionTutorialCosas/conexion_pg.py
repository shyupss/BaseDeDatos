import psycopg2

# Conexión a PostgreSQL
conn = psycopg2.connect(
	host="localhost",
	database="tutorialpython",
	user="pythonuser",
	password="1234"
)

cur = conn.cursor()

# Crear una tabla de ejemplo
cur.execute("""
	CREATE TABLE IF NOT EXISTS ejemplo (
    	id SERIAL PRIMARY KEY,
    	nombre VARCHAR(100)
	);
""")
conn.commit()

# Insertar datos
cur.execute("INSERT INTO ejemplo (nombre) VALUES (%s)", ("Juan",))
conn.commit()

# Consultar datos
cur.execute("SELECT * FROM ejemplo;")
filas = cur.fetchall()
for fila in filas:
	print(fila)

# Cerrar conexión
cur.close()
conn.close()