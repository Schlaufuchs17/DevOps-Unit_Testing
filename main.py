from fastapi import FastAPI
from pathlib import Path
app = Flask(__name__)

@app.post("/Almacenar")
def add(string):
    dataBase = open("registro.txt", "a")
    dataBase.write(string + "\n")
    dataBase.close()
    return {"Respuesta" : "Se ha creado correctamente"}

@app.get("/Consultar")
def buscar(string):
    file = Path('registro.txt') # Se creara el fichero en caso de que no exista anteriormente
    file.touch(exist_ok=True)
    dataBase = open("registro.txt", "r").read().splitlines()
    i = 0
    a,b = 'áéíóú','aeiou' # Se eliminarian las tildes en caso de que fuera necesario con "maketrans"

    trans = str.maketrans(a,b) # Metodo que sirve para traducir
    for line in dataBase:
	    new_line = line.lower() # No tendria en cuenta las minusculas
	    new_line = new_line.translate(trans)
	    if (string in new_line):
		    i += 1 
    print(i)	
    return {"Numero" : i}

@app.get("/")
def read_root():
    return {"Todo correcto!"}

if __name__ == "__main__":
    uvicorn.run(app, port=12345, host="127.0.0.1")