import logging
from fastapi import APIRouter, HTTPException
from src.model.Datos import Datos

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

datos = APIRouter()

@datos.post("/", status_code=201)
def datos_post(datos: Datos):
    try:
        logger.info("Processing request with data: %s", datos)
        response = {
            "zona_exclusion": datos.calcular_zona_exclusion(),
            "zona_ocupacion": datos.calcular_zona_ocupacion(),
            "zona_poblacion": datos.calcular_zona_poblacion()
        }
        logger.info("Successfully processed data")
        return response
    except ValueError as ve:
        logger.error("ValueError occurred: %s", ve)
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        logger.error("Unhandled exception occurred: %s", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
