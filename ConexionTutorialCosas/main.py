from fastapi import FastAPI, HTTPException
import psycopg2

app = FastAPI()

# Conexión a PostgreSQL
conn = psycopg2.connect(
	host="localhost",
	database="tutorialpython",
	user="pythonuser",
	password="1234"
)
cur = conn.cursor()

# Ruta raíz
@app.get("/")
def home():
	return {"mensaje": "Bienvenido a la API de tutorialpython!!"}

# Ruta GET simple
@app.get("/saludo/{nombre}")
def saludar(nombre: str):
	return {"mensaje": f"Hola, {nombre}!"}

# Ruta POST para agregar un periodista
@app.post("/periodistas/")
def agregar_periodista(nombre: str, email: str):
	try:
		cur.execute("INSERT INTO periodistas (nombre, email) VALUES (%s, %s)", (nombre, email))
		conn.commit()
		return {"mensaje": "Periodista agregado correctamente"}
	except Exception as e:
		conn.rollback()
		raise HTTPException(status_code=500, detail=str(e))

# Ruta GET para obtener todos los periodistas
@app.get("/periodistas/")
def listar_periodistas():
	cur.execute("SELECT id, nombre, email FROM periodistas")
	rows = cur.fetchall()
	return [{"id": r[0], "nombre": r[1], "email": r[2]} for r in rows]

# Ruta PUT para actualizar un periodista
@app.put("/periodistas/{id}")
def actualizar_periodista(id: int, nombre: str, email: str):
	try:
		cur.execute("UPDATE periodistas SET nombre = %s, email = %s WHERE id = %s", (nombre, email, id))
		conn.commit()
		return {"mensaje": "Periodista actualizado correctamente"}
	except Exception as e:
		conn.rollback()
		raise HTTPException(status_code=500, detail=str(e))