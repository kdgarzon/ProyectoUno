import math
from pydantic import BaseModel

class Datos(BaseModel):
    frecuencia: float  # en MHz
    potencia: float    # Watts PIRE
    altura: float      # en metros

    def calcular_zona_exclusion(self):
        return self.calcular_zona_ocupacion() / 2

    def calcular_zona_ocupacion(self):
        r = 0
        if self.frecuencia >= 1 and self.frecuencia < 10:
            r = 0.0144 * self.frecuencia * math.sqrt(self.potencia)
        elif self.frecuencia >= 10 and self.frecuencia < 400:
            r = 0.143 * math.sqrt(self.potencia)
        elif self.frecuencia >= 400 and self.frecuencia < 2000:
            r = 2.92 * math.sqrt(self.potencia / self.frecuencia)
        elif self.frecuencia >= 2000 and self.frecuencia < 300000:
            r = 0.0638 * math.sqrt(self.potencia)
            
        if self.altura >= r:
            return r
        
        distancia = math.sqrt((r**2) - (self.altura**2))
        return distancia

    def calcular_zona_poblacion(self):
        r = 0
        if self.frecuencia >= 1 and self.frecuencia < 10:
            r = 0.10 * math.sqrt(self.potencia * self.frecuencia)
        elif self.frecuencia >= 10 and self.frecuencia < 400:
            r = 0.319 * math.sqrt(self.potencia)
        elif self.frecuencia >= 400 and self.frecuencia < 2000:
            r = 6.38 * math.sqrt(self.potencia / self.frecuencia)
        elif self.frecuencia >= 2000 and self.frecuencia < 300000:
            r = 0.143 * math.sqrt(self.potencia)
            
        if self.altura >= r:
            return r
        
        distancia = math.sqrt((r**2) - (self.altura**2)) 
        return distancia