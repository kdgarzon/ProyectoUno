from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from src.model.Datos import Datos

# Definimos el modelo de datos que recibirá el POST


# Creamos la instancia de la aplicación FastAPI
app = FastAPI()

# Habilitar CORS para todos los orígenes
origins = ["*"]  # Permite todos los orígenes

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permitir todos los orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permite todas las cabeceras
)

# Definimos el endpoint POST
@app.post("/datos")
def recibir_datos(datos: Datos):
    
    try:
        return {
        "zona_exclusion": datos.calcular_zona_exclusion(),
        "zona_ocupacion": datos.calcular_zona_ocupacion(),
        "zona_poblacion": datos.calcular_zona_poblacion()
        }
    except Exception as e:
        raise e
    #zona_exclusion = datos.altura * datos.frecuencia
    
    

